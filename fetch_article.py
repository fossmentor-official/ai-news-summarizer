# fetch_article.py
from newspaper import Article

def fetch_article_text(url: str) -> dict:
    """Fetches article text and metadata from a given URL."""
    a = Article(url)
    a.download()
    a.parse()
    return {
        "title": a.title,
        "authors": a.authors,
        "publish_date": a.publish_date,
        "text": a.text
    }
