from flask import Flask, render_template
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html", email = os.getenv("EMAIL"), phone = os.getenv("PHONE"), address = os.getenv("ADDRESS")
)


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
