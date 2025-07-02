# To run backend server, type the following into your TERMINAL:
# cd \Users\gwant\OneDrive\Documents\VSCode\MoodPredictor\BackEnd
# - then type -
# python app.py

from flask import Flask, request, jsonify
from flask_cors import CORS 

app = Flask(__name__)
CORS(app)

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json 
    text = data.get("text", "").lower()

    if "happy" in text or "great" in text or "fantastic" in text or "good" in text:
        mood = "happy"
    elif "sad" in text or "upset" in text or "bad" in text or "shit" in text or "ass" in text:
        mood = "sad"
    else:
        mood = "neutral"

    return jsonify({"mood": mood})

if __name__ == '__main__':
    app.run(debug=True)