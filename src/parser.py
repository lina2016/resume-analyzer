# src/parser.py
import pdfplumber

def extract_text_from_pdf(pdf_path: str) -> str:
    """
    Extract text from a PDF resume.
    """
    text = ""
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            text += page.extract_text() or ""
    return text.strip()
