# cli.py
import argparse
from fetch_article import fetch_article_text
from summarizer import load_summarizer, summarize_text

def main():
    p = argparse.ArgumentParser()
    p.add_argument("--url", help="Article URL to summarize")
    p.add_argument("--file", help="Local text file to summarize")
    p.add_argument("--model", default="facebook/bart-large-cnn")
    p.add_argument("--max_len", type=int, default=130)
    p.add_argument("--min_len", type=int, default=30)
    args = p.parse_args()

    if not args.url and not args.file:
        print("Provide --url or --file")
        return

    if args.url:
        article = fetch_article_text(args.url)
        text = article["text"]
        print("Title:", article["title"])
    else:
        with open(args.file, "r", encoding="utf-8") as f:
            text = f.read()

    summarizer = load_summarizer(model_name=args.model)
    summary = summarize_text(text, summarizer, max_length=args.max_len, min_length=args.min_len)
    print("\n==== Summary ====\n", summary)

if __name__ == "__main__":
    main()
