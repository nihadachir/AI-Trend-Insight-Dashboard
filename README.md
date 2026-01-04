# 🚀 AI Trend Insights Platform

An end-to-end automated data pipeline designed to monitor, analyze, and visualize trends in Artificial Intelligence news and research.

The system collects AI-related content, performs basic NLP analysis (keywords & sentiment), stores structured data, and delivers automated visual reports via Looker Studio.

This project demonstrates practical skills in **data engineering, automation, NLP, and BI reporting**, using only **free tools**.

---

## 🎯 Project Objectives

- Automatically collect AI-related articles and research content
- Clean and normalize textual data
- Extract keywords and sentiment indicators
- Store structured insights for analysis
- Visualize trends through an interactive dashboard
- Automatically distribute reports via email (PDF)

---

## 🧱 Architecture Overview

Cron Trigger (n8n) -> External APIs (AI News / Research) -> Data Cleaning & Normalization -> Keyword Extraction & Sentiment Analysis -> Google Sheets (Data Storage) -> Looker Studio(Visualization & Reporting) -> Scheduled PDF Report via Email


---

## 🛠️ Technologies Used

- **n8n** – Workflow automation and orchestration
- **APIs** – AI-related news and research sources
- **NLP (basic)** – Keyword extraction & sentiment analysis
- **Google Sheets** – Data storage layer
- **Looker Studio** – Dashboard creation & scheduled reporting
- **JavaScript** – Data transformation inside n8n
- **GitHub** – Version control & documentation

---

## 📊 Dataset Schema

The main dataset stored in Google Sheets (`AI_Trend_Insights`) includes:

| Column | Description |
|------|------------|
| title | Article or paper title |
| summary | Cleaned text summary |
| keywords | Extracted keywords |
| sentiment | Sentiment label (Positive / Neutral / Negative) |
| sentiment_score | Numeric sentiment score (-1, 0, 1) |
| source | Content source |
| url | Original content URL |
| year | Publication year |

---

## 📈 Dashboard & Visualizations

The Looker Studio dashboard includes:

- **Keyword frequency analysis**
- **Sentiment distribution (Positive / Neutral / Negative)**
- **Sentiment evolution over time**
- **Top content sources**
- **Table of recent or negative-sentiment articles**

📊 The dashboard is connected live to Google Sheets and updates automatically.

🔗 Public dashboard link:  
`https://lookerstudio.google.com/s/vYySo4ggD8g`

---

## 📧 Automated Reporting

Reports are automatically generated and distributed using **Looker Studio’s native email scheduling feature**.

- Format: **PDF**
- Frequency: Daily / Weekly (configurable)
- Content: Full dashboard with charts and tables
- No manual intervention required

This ensures continuous monitoring and easy sharing of insights with stakeholders.

---

## 💡 Key Features

- Fully automated data pipeline
- Clear separation between data processing and visualization
- Uses only free and widely adopted tools
- Scalable and easily extensible
- Portfolio-ready and industry-oriented

---

## 📌 Use Cases

- AI technology watch (veille technologique)
- Trend analysis for innovation teams
- Sentiment monitoring of AI-related topics
- BI reporting automation
- Data engineering & analytics portfolio project

---

## 🚀 Future Improvements

- Advanced NLP (TF-IDF, embeddings, topic modeling)
- Real-time alerts based on sentiment spikes
- Source credibility scoring
- Daily/weekly trend comparison
- Public REST API for insights access

---

## 👤 Author

**Nihad Achir**  
Data Science & AI Enthusiast  

🔗 LinkedIn: 
https://www.linkedin.com/in/nihad-achir-191888299

---

## ⭐ Support

If you find this project interesting, feel free to ⭐ star the repository or fork it to build your own automated insight platform.
