from transformers import pipeline
from newspaper import Article
import torch


class NewsSummarizer:
    def __init__(self, model_name: str = "facebook/bart-large-cnn"):
        """
        Initialize the summarization pipeline.
        Defaults to BART-Large-CNN, ideal for news-style summarization.
        """
        device = 0 if torch.cuda.is_available() else -1
        self.summarizer = pipeline("summarization", model=model_name, device=device)

    def fetch_article_text(self, url: str) -> str:
        """
        Extracts and returns clean text from a news article URL.
        """
        article = Article(url)
        article.download()
        article.parse()
        return article.text.strip()

    def chunk_text(self, text: str, chunk_size: int = 700) -> list:
        """
        Splits long text into smaller chunks of approx `chunk_size` words.
        Ensures no empty chunks are included.
        """
        words = text.split()
        chunks = []
        for i in range(0, len(words), chunk_size):
            chunk = ' '.join(words[i:i + chunk_size]).strip()
            if chunk:
                chunks.append(chunk)
        return chunks

    def summarize_text(self, text: str, max_len: int = 200, min_len: int = 60) -> str:
        """
        Summarizes given text safely, splitting into chunks if too long.
        Returns the combined summary.
        """
        chunks = self.chunk_text(text)
        summaries = []
        for chunk in chunks:
            if len(chunk.split()) < 10:  # skip very small chunks
                continue
            summary = self.summarizer(
                chunk,
                max_length=max_len,
                min_length=min_len,
                do_sample=False
            )[0]["summary_text"]
            summaries.append(summary)
        return ' '.join(summaries)

    def summarize_from_url(self, url: str) -> dict:
        """
        Combines fetching + summarization in one go.
        Returns a dict with 'text' and 'summary'.
        """
        text = self.fetch_article_text(url)
        if not text or len(text.split()) < 50:
            raise ValueError("Insufficient text extracted from the URL.")
        summary = self.summarize_text(text)
        return {"text": text, "summary": summary}
