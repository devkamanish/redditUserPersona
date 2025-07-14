from jinja2 import Template
import markdown

html_template = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Reddit Persona - {{ username }}</title>
    <style>
        body {
            font-family: 'Segoe UI', sans-serif;
            background: #f4f4f4;
            padding: 2rem;
            max-width: 960px;
            margin: auto;
            color: #333;
        }
        h1 {
            text-align: center;
            color: #2a2a2a;
        }
        .content {
            background: white;
            border-radius: 12px;
            padding: 2rem;
            box-shadow: 0 0 15px rgba(0, 0, 0, 0.1);
        }
        h2, h3 {
            color: #444;
            border-bottom: 1px solid #ddd;
            padding-bottom: 0.3rem;
        }
        img {
            max-width: 100%;
            border-radius: 10px;
            margin-top: 1rem;
            box-shadow: 0 0 5px rgba(0,0,0,0.05);
        }
        ul {
            padding-left: 1.5rem;
        }
        p {
            margin: 1rem 0;
        }
    </style>
</head>
<body>
    <h1>🧑 Reddit User Persona: {{ username }}</h1>
    <div class="content">
        {{ content | safe }}

        <h2>📊 Word Cloud</h2>
        <img src="{{ username }}_wordcloud.png" alt="Word Cloud">

        <h2>😊 Sentiment Analysis</h2>
        <img src="{{ username }}_sentiment.png" alt="Sentiment Chart">
    </div>
</body>
</html>
"""

def save_persona_as_html(username, persona_text):
    html_content = markdown.markdown(persona_text)

    template = Template(html_template)
    final_html = template.render(username=username, content=html_content)

    with open(f"personas/{username}.html", "w") as f:
        f.write(final_html)