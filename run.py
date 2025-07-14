import argparse
import os
from reddit_scraper import get_user_data
from llm_utils import generate_persona
from formatter import save_persona_as_html
from analysis import generate_wordcloud, generate_sentiment_chart

def extract_username(profile_url):
    return profile_url.rstrip('/').split('/')[-1]

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate Reddit user persona")
    parser.add_argument("url", help="Reddit user profile URL")
    parser.add_argument("--html", action="store_true", help="Also export persona to HTML")
    args = parser.parse_args()

    username = extract_username(args.url)
    print(f"Fetching Reddit data for {username}...")

    data = get_user_data(username)

    text_blocks = [p['title'] + " " + p['body'] for p in data['posts']] + [c['body'] for c in data['comments']]
    full_text = "\n\n".join(text_blocks)

    print("Generating persona with LLaMA 3...")
    try:
        persona = generate_persona(full_text)
    except Exception as e:
        print("LLM call failed:", e)
        exit(1)

    os.makedirs("personas", exist_ok=True)
    with open(f"personas/{username}.txt", "w") as f:
        f.write(persona)
    print("Saved persona as text.")

    if args.html:
        save_persona_as_html(username, persona)
        print("Saved persona as HTML.")

    generate_wordcloud(full_text, username)
    generate_sentiment_chart(text_blocks, username)