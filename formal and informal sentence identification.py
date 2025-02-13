from flask import Flask, render_template, request, jsonify
import nltk
from nltk.corpus import stopwords
import string
import random

# Download necessary NLTK data
nltk.download('stopwords')

app = Flask(__name__)

# Dummy classifier function for detecting formal vs informal
def classify_sentence(sentence):
    # Simple logic based on the sentence's style and words
    formal_keywords = ["please", "kindly", "regards", "sincerely"]
    informal_keywords = ["hey", "yo", "wanna", "gonna"]
    
    sentence = sentence.lower()
    
    if any(word in sentence for word in formal_keywords):
        return "Formal"
    elif any(word in sentence for word in informal_keywords):
        return "Informal"
    else:
        # Fallback for sentences not detected as either type
        return random.choice(["Formal", "Informal"])

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/check_sentence", methods=["POST"])
def check_sentence():
    data = request.get_json()
    sentence = data['sentence']
    sentence_type = classify_sentence(sentence)
    return jsonify({"type": sentence_type})

if __name__ == "__main__":
    app.run(debug=True)