# 📰 AI Article Summarizer — Intelligent Content Digestion for Business Teams

> **Turn any article URL into a concise, actionable summary in seconds — powered by Facebook's BART transformer model, with a REST API ready for integration into your existing tools.**

Business teams — in eCommerce, healthcare, and SaaS — consume enormous volumes of online content daily: competitor news, industry reports, supplier updates, regulatory changes. Reading everything manually is not scalable.

This tool solves that. Paste any article URL and get a clean, accurate summary instantly. Built for both end-users via a web interface and developers via a REST API, it fits into existing workflows without friction.

---

## 💡 Business Use Cases

- **eCommerce Teams** — Summarize competitor product launches, supplier announcements, and market trend articles without leaving your workflow
- **Healthcare & Compliance** — Digest regulatory updates, clinical research abstracts, or policy documents quickly
- **Content & Marketing Teams** — Monitor industry news at scale; get the key points without reading every article in full
- **SaaS Product Teams** — Summarize customer feedback articles, competitor changelog posts, or analyst reports for internal briefings
- **Knowledge Management** — Feed article summaries into internal wikis, reports, or team digests automatically via the API

---

## 🚀 Features

- Summarizes any article from a URL — no manual copy-paste required
- Powered by **Facebook BART-large-CNN**, a production-grade summarization model
- **REST API endpoint** (Flask) — integrate directly into your SaaS platform, CRM, or internal tooling
- **CLI support** — scriptable for batch processing and automated pipelines
- Clean **Streamlit web interface** — usable by non-technical business users
- Fully containerized with Docker — deploy on any cloud environment in minutes
- CPU-compatible — no GPU infrastructure required

---

## 🏗️ Tech Stack

| Layer | Technology |
|---|---|
| AI Model | HuggingFace Transformers — Facebook BART-large-CNN |
| Article Extraction | newspaper3k |
| Backend API | Flask (REST endpoint for integrations) |
| Frontend | Streamlit |
| CLI | Python argparse |
| Containerization | Docker / Dev Containers |
| Deployment | Any cloud — AWS, GCP, DigitalOcean (CPU-based) |

---

## ⚙️ Installation

### Option 1 — Dev Container (Recommended)

1. Clone the repository:
```bash
git clone https://github.com/fossmentor-official/ai-news-summarizer.git
cd ai-news-summarizer
```

2. Open in **VS Code** or **Cursor** and click **"Reopen in Container"**

3. Wait for Docker to build — environment opens automatically inside the container

4. Run the Streamlit app:
```bash
streamlit run app.py
```

5. Open your browser at `http://localhost:8501`

### Option 2 — CLI (Batch / Automation Use)

```bash
python cli.py --url https://example.com/article-url
```

Ideal for scripted pipelines, scheduled jobs, or integration into larger automation workflows.

### Option 3 — REST API (Integration Use)

Start the Flask API server and send POST requests with an article URL. Returns a structured JSON summary — ready to consume in any backend system.

---

## 🖥️ Usage

1. Paste any article URL into the input field
2. Click **"Summarize"**
3. Receive a clean, concise summary of the article content

---

## 🗺️ Roadmap

- [ ] Batch URL processing — summarize multiple articles in a single API call
- [ ] Scheduled monitoring — auto-summarize RSS feeds or news sources on a cron schedule
- [ ] Summary storage — save results to PostgreSQL or MongoDB for searchable archive
- [ ] Webhook support — push summaries to Slack, Teams, or internal dashboards automatically
- [ ] Custom summary length control — brief / standard / detailed output modes
- [ ] Multi-language article support

---

## 🤝 Built by Wasif Younas

**AI Automation & Solutions Architect** with 12+ years of experience building production-grade systems across healthcare SaaS, eCommerce, and ERP platforms.

This project demonstrates how transformer-based NLP can be embedded into real business workflows via clean APIs — not just standalone demos. The Flask REST endpoint is intentionally designed for integration into existing SaaS or internal tooling with minimal engineering effort.

**Want this integrated into your platform or customized for your workflow?**

[![LinkedIn](https://raw.githubusercontent.com/MartinHeinz/MartinHeinz/master/linkedin-3-16.png)](https://www.linkedin.com/in/fossmentor/)
[![Facebook](https://i.imgur.com/dqSkGWu.png)](https://facebook.com/fossmentor)
[![Instagram](https://i.imgur.com/TFy6wii.png)](https://www.instagram.com/fossmentor.official/)

📧 contact@fossmentor.com | 🌐 [fossmentor.com](https://fossmentor.com)

---

## 🪪 License

MIT License © 2025 Wasif Younas — [fossmentor.com](https://fossmentor.com)
