import requests

def generate_persona(text, model="llama3.2"):
    prompt = f"""
    You are an AI that builds user personas from Reddit activity.

    Below is a Reddit user's posts and comments. Based on the content,
    create a detailed user persona including:
    - Bio Summary
    - Interests
    - Writing Style / Tone
    - Political or Ideological Leaning
    - Top Subreddits
    - Citations (quotes or post links for each trait)

    Be specific and cite actual quotes or paraphrased Reddit posts.

    Text:
    {text[:4000]}  # truncate for short models
    """

    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": model,
            "prompt": prompt,
            "stream": False
        }
    )

    if response.status_code == 200:
        return response.json()["response"]
    else:
        raise Exception(f"Ollama error: {response.status_code} - {response.text}")