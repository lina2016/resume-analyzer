# 📄 AI-Powered Resume Analyzer (NLP + Transformers)

An **AI-driven Resume Analyzer** built with **Python**, **Natural Language Processing (NLP)**, and **Transformer embeddings** to evaluate how well a resume aligns with a job description.
This project uses **Sentence Transformers** to compute semantic similarity and provides an intelligent match score, missing keyword suggestions, and section-wise analysis.

---

## 🌟 Live Demo
🚀 **Coming soon on Streamlit Cloud!**
(You can deploy your own version easily using Streamlit Cloud or Render.)

---

## 👩‍💻 Author
**Lina Jamadar**
AI Engineer | Python Developer | Full-Stack Web Developer
📍 Surat, Gujarat, India
🔗 [LinkedIn](https://www.linkedin.com/in/lina-jamadar) | [GitHub](https://github.com/lina2016)

---

## 🚀 Features
- 🧠 **AI-Powered Semantic Analysis** — Uses pretrained Transformer model `all-MiniLM-L6-v2` to understand text meaning, not just keywords.
- 📑 **PDF Resume Parsing** — Extracts and processes text from uploaded resume PDFs.
- 🔍 **Smart Resume–Job Comparison** — Computes cosine similarity between embeddings for accurate match scoring.
- 📊 **Section-wise Insights** — Analyzes *Skills*, *Experience*, and *Education* separately.
- 💡 **Keyword Gap Detection** — Suggests missing technical skills and action verbs.
- 🌐 **Interactive UI** — Built with **Streamlit** for simple, beautiful web deployment.

---

## 🧰 Tech Stack
| Category | Tools / Libraries |
|-----------|-------------------|
| Language | Python 3.9+ |
| NLP Model | SentenceTransformers (`all-MiniLM-L6-v2`) |
| ML Tools | scikit-learn, numpy |
| Text Extraction | pdfplumber |
| Web App | Streamlit |
| Others | re, cosine similarity, data preprocessing |

---

## ⚙️ Installation & Usage

### 1️⃣ Clone the Repository
git clone https://github.com/lina2016/resume-analyzer.git
cd resume-analyzer

### 2️⃣ Install Dependencies
pip install -r requirements.txt

### 3️⃣ Run the Application
streamlit run src/app.py

### 4️⃣ Access the App

Visit 👉 http://localhost:8501 in your browser.

🧾 Example Output

✅ Overall Match Score: 72.4%

📊 Section-wise Match:
Skills: 80.1%
Experience: 68.3%
Education: 59.2%

🔑 Missing Keywords:
rust, typescript, copilot, codex, collaborate, build, debug

📂 Project Structure
resume-analyzer/
│── src/
│   ├── parser.py          # Extracts text from resume PDFs
│   ├── analyzer.py        # Core NLP, embeddings, and scoring logic
│   └── app.py             # Streamlit UI
│── data/
│   ├── sample_resume.pdf
│   └── sample_job_description.txt
│── requirements.txt
│── README.md
│── .gitignore
│── LICENSE

🧠 Behind the Scenes
This application leverages pretrained transformer models to perform semantic text analysis between two unstructured documents.
It demonstrates key AI/NLP techniques including:

Sentence embeddings

Cosine similarity for semantic matching

Keyword extraction & filtering

Section-based text analytics

Interactive UI deployment with Streamlit

✅ It’s an Applied AI project showcasing both machine learning understanding and software engineering capability.

🧩 Future Enhancements

-🤖 Integrate LLM feedback (e.g., GPT-based resume improvement tips)

-🔗 Connect with Jooble API for live job data

-🧱 Add NER-based skill extraction using spaCy

-☁️ Deploy live demo on Streamlit Cloud


🧾 License

This project is licensed under the MIT License.
Feel free to use, modify, and share it — just credit the author.

💬 Contact

If you found this project helpful or want to collaborate:

📧 linajamadar@gmail.com

🔗 LinkedIn : https://www.linkedin.com/in/lina-jamadar/
 | GitHub : https://github.com/lina2016

⭐ If you like this project, please consider giving it a star on GitHub!
It helps others discover this work and supports open-source learning.

## Screenshots
![Screenshot](data/result.png)
