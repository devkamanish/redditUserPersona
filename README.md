# 🧠 Reddit User Persona Generator

This is a Python project that scrapes a Reddit user's posts and comments and uses a local LLM (like LLaMA 3 via Ollama) to generate a detailed **User Persona**. The output includes a text profile, an optional HTML dashboard, and NLP-based visualizations like a **word cloud** and **sentiment analysis** chart.

---

## ✨ Features

- 🔍 Scrapes Reddit posts & comments using PRAW
- 🧠 Uses **LLaMA 3 locally** (via Ollama) to generate personas
- 📄 Outputs persona as `.txt` and `.html`
- 📊 Generates word cloud and sentiment bar chart
- ⚡ Fast, free (no OpenAI key required), local-first

---

## 🛠️ Setup Instructions

### 1. ✅ Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/reddit-user-persona.git
cd reddit-user-persona
```

### 2. ✅ Create a virtual environment

```bash
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
```

### 3. ✅ Install dependencies

```bash
pip install -r requirements.txt
```

### 4. ✅ Create your `.env` file for Reddit API

```env
REDDIT_CLIENT_ID=your_client_id
REDDIT_CLIENT_SECRET=your_client_secret
REDDIT_USER_AGENT=PersonaGeneratorScript by /u/your_reddit_username
```

> You can get your Reddit API keys by creating a Reddit app here: https://www.reddit.com/prefs/apps

---

## 🤖 LLM Setup (Ollama + LLaMA 3)

> This project assumes you’re using **[Ollama](https://ollama.com)** to run LLaMA 3 locally.

### Install Ollama:

```bash
curl -fsSL https://ollama.com/install.sh | sh
```

### Download and run LLaMA 3:

```bash
ollama pull llama3.2
ollama run llama3.2
```

You must have `ollama run llama3.2` running **in the background** while generating personas.

---

## 🚀 How to Use

```bash
python run.py https://www.reddit.com/user/kojied/ --html
```

### Arguments:

- `url` — Reddit user profile URL
- `--html` — Optional: also generate an HTML dashboard

---

## 📂 Output Structure

All outputs are saved in the `/personas/` folder:

```
personas/
├── kojied.txt              ← LLM-generated persona text
├── kojied.html             ← Optional dashboard-style HTML output
├── kojied_wordcloud.png    ← Word cloud of most frequent words
├── kojied_sentiment.png    ← Sentiment bar chart (positive/neutral/negative)
```

---

## 👤 Example Persona Output

**User**: `https://www.reddit.com/user/kojied/`  
**Persona**:

- 📌 Age Group: Mid 20s–30s
- 🎯 Interests: Urban lifestyle, nightlife, city culture
- ✍️ Style: Longform, introspective, narrative
- ⚖️ Leaning: Socially liberal, thoughtful
- 📎 Citations: [Link to comments/posts included in output]

---

## 💡 Notes

- Make sure your Reddit API keys are working — PRAW will raise errors otherwise.
- If you get an LLM error, confirm that Ollama is running in a separate terminal.
- The script handles up to 50 posts and 50 comments per user (can be modified).

---

## 👩‍💻 Author

Made with ❤️ by Manish Devka

---

## ✅ License

This is an educational assignment submission and not intended for commercial use. All code is your property.#
