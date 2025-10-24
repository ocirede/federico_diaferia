from flask import Flask, render_template, request, redirect, url_for
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)

@app.route('/')
def home():
    # Redirect to English portfolio by default
    return redirect(url_for('portfolio', lang='en'))

@app.route('/<lang>')
def portfolio(lang):
    # Detect if user is on mobile
    user_agent = request.headers.get("User-Agent", "").lower()
    is_mobile = "mobi" in user_agent or "android" in user_agent

    # Pass .env variables and mobile info to template
    template_vars = {
        "is_mobile": is_mobile,
        "email": os.getenv("EMAIL"),
        "phone": os.getenv("PHONE"),
        "address": os.getenv("ADDRESS")
    }

    if lang == 'de':
        return render_template('index.de.html', **template_vars)
    return render_template('index.en.html', **template_vars)

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)

