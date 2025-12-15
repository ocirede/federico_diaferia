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
    user_agent = request.headers.get("User-Agent", "").lower()
    is_mobile = "mobi" in user_agent or "android" in user_agent

    email = os.getenv("EMAIL", "")
    email_user, email_domain = email.split("@")
    email_domain_name, email_tld = email_domain.split(".")

    phone = os.getenv("PHONE", "")
    phone_parts = [
        phone[:3],
        phone[3:6],
        phone[6:9],
        phone[9:]
    ]
    address = os.getenv("ADDRESS", "")
    address_parts = address.split(".")
    template_vars = {
        "is_mobile": is_mobile,
        "email_parts": [email_user, email_domain_name, email_tld],
        "phone_parts": phone_parts,
        "address_parts": address_parts,
    }

    if lang == 'de':
        return render_template('index.de.html', **template_vars)
    return render_template('index.en.html', **template_vars)


if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)

