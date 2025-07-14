from wordcloud import WordCloud
import matplotlib.pyplot as plt
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import os

def generate_wordcloud(text, username):
    wc = WordCloud(
        width=800, height=400,
        background_color='white',
        max_words=100
    ).generate(text)

    path = f"personas/{username}_wordcloud.png"
    wc.to_file(path)
    print(f"Word cloud saved to {path}")

def generate_sentiment_chart(text_blocks, username):
    analyzer = SentimentIntensityAnalyzer()

    sentiment_counts = {"positive": 0, "neutral": 0, "negative": 0}
    for block in text_blocks:
        score = analyzer.polarity_scores(block)["compound"]
        if score >= 0.05:
            sentiment_counts["positive"] += 1
        elif score <= -0.05:
            sentiment_counts["negative"] += 1
        else:
            sentiment_counts["neutral"] += 1

    labels = list(sentiment_counts.keys())
    values = list(sentiment_counts.values())

    plt.figure(figsize=(6,4))
    bars = plt.bar(labels, values, color=["green", "gray", "red"])
    plt.title("Sentiment Breakdown")
    plt.ylabel("Number of Posts/Comments")
    plt.tight_layout()

    path = f"personas/{username}_sentiment.png"
    plt.savefig(path)
    print(f"Sentiment chart saved to {path}")
    plt.close()