from fastapi import FastAPI
from pydantic import BaseModel
from transformers import pipeline

app = FastAPI(title="Summarizer API")

class Article(BaseModel):
    text: str

summarizer = pipeline(
    "summarization",
    model="sshleifer/distilbart-cnn-12-6"
)

@app.post("/summarize")
def summarize(article: Article):
    result = summarizer(article.text, max_length=150, min_length=40)
    return {"summary": result[0]["summary_text"]}
