# src/analyzer.py

import re
import numpy as np
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import ENGLISH_STOP_WORDS

# Load sentence embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")

# Define sections you want to analyze separately
sections = ["skills", "experience", "education"]

# Optional: relevant technical and action keywords
TECH_KEYWORDS = [
    "python", "rust", "typescript", "javascript", "ai", "ml", "deep learning",
    "docker", "aws", "git", "api", "fastapi", "flask", "tensorflow", "pytorch",
    "copilot", "codex", "claude", "openai", "streamlit", "fastapi", "remote"
]

ACTION_WORDS = [
    "build", "debug", "collaborate", "evaluate", "develop",
    "implement", "contribute", "review", "improve"
]


# ----------------------- Core Utility Functions -----------------------

def clean_text(text: str) -> str:
    """Clean and normalize text for embedding."""
    text = re.sub(r'\s+', ' ', text)
    return text.strip().lower()


def compute_similarity(resume_text: str, jd_text: str) -> float:
    """Compute cosine similarity between resume and job description embeddings."""
    resume_emb = model.encode([clean_text(resume_text)])
    jd_emb = model.encode([clean_text(jd_text)])
    similarity = cosine_similarity(resume_emb, jd_emb)[0][0]
    return round(float(similarity) * 100, 2)


def find_missing_keywords(resume_text: str, jd_text: str, top_n: int = 15):
    """Find keywords in the job description that are not in the resume."""
    resume_words = set(clean_text(resume_text).split()) - ENGLISH_STOP_WORDS
    jd_words = set(clean_text(jd_text).split()) - ENGLISH_STOP_WORDS
    missing = [w for w in jd_words - resume_words if len(w) > 2 and w.isalpha()]
    return missing[:top_n]


def filter_relevant_keywords(missing_words):
    """Filter missing words to only keep relevant tech/action keywords."""
    relevant = [
        word for word in missing_words
        if word.lower() in TECH_KEYWORDS or word.lower() in ACTION_WORDS
    ]
    return relevant

def expand_education_text(text: str) -> str:
    """Add context so the model has richer embeddings."""
    if len(text.split()) < 30:
        text += (
            " This section lists formal degrees and professional certifications "
            "including AI, machine learning, Python, cloud computing, and software engineering."
        )
    return text

# ----------------------- Section Analysis -----------------------

def compute_section_scores(resume_text: str, jd_text: str):
    """
    Computes similarity for each section (skills, experience, education)
    against the job description.
    """
    section_scores = {}

    for sec in sections:
        pattern = rf"{sec}\s*:?([\s\S]*?)(?=\n[A-Z][a-zA-Z ]+:|$)"
        match = re.search(pattern, resume_text, re.IGNORECASE)
        if sec.lower() == "education":
            section_text = expand_education_text(section_text)

        if match:
            section_text = match.group(1)
            score = compute_similarity(section_text, jd_text)
            section_scores[sec.capitalize()] = score
        else:
            section_scores[sec.capitalize()] = 0.0  # Section not found
    return section_scores
