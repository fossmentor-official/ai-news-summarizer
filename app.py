import streamlit as st
from summarizer import NewsSummarizer

# Cache model for performance
@st.cache_resource
def get_summarizer():
    return NewsSummarizer()

summarizer = get_summarizer()

st.set_page_config(page_title="News Summarizer", page_icon="📰", layout="centered")
st.title("📰 News Summarizer")
st.markdown("### Summarize any news article or text using AI")

# 1️⃣ Option: Paste text
st.subheader("Paste the article text directly")
user_text = st.text_area("Enter the text you want to summarize:", height=250)

if st.button("Summarize Text"):
    if not user_text.strip() or len(user_text.split()) < 20:
        st.warning("⚠️ Please enter at least 20 words for summarization.")
    else:
        with st.spinner("Summarizing text... 🧠"):
            try:
                # Automatically handles long text via chunking
                summary = summarizer.summarize_text(user_text)
                st.subheader("🧠 Generated Summary")
                st.success(summary)
            except Exception as e:
                st.error(f"⚠️ Error during summarization: {str(e)}")

# 2️⃣ Option: Summarize from URL
st.markdown("---")
st.subheader("Or summarize from URL")
url = st.text_input("Enter a news article URL:")

if st.button("Summarize Article from URL"):
    if not url.strip():
        st.warning("⚠️ Please enter a valid URL.")
    else:
        from newspaper import Article
        try:
            with st.spinner("Fetching and summarizing the article... 📰"):
                article = Article(url)
                article.download()
                article.parse()
                text = article.text

                if len(text.split()) < 50:
                    st.error("⚠️ Could not extract enough text from this URL.")
                else:
                    # Summarize text in safe chunks
                    summary = summarizer.summarize_text(text)

                    st.subheader("🧾 Original Article (Truncated)")
                    st.text_area(
                        "Full Article",
                        text[:1000] + "..." if len(text) > 1000 else text,
                        height=250
                    )

                    st.subheader("🧠 Generated Summary")
                    st.success(summary)
        except Exception as e:
            st.error(f"⚠️ Error: {str(e)}")
