from flask import Flask, request, jsonify, render_template
from google import genai
import os

app = Flask(__name__)

# ✅ Create Gemini client
client = genai.Client(api_key="AIzaSyBOsI3P9rYr7bD2XhdXWUjsIxWD8PiGXD8")


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    prompt = data.get("message", "")

    response = client.models.generate_content(
        model="gemini-3-pro-preview",
        contents=prompt
    )

    return jsonify({"reply": response.text})


if __name__ == "__main__":
    app.run(port=3000, debug=True)