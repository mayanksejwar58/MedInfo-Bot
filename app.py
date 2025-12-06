from flask import Flask, render_template,request, jsonify,redirect,url_for
from google import genai
from dotenv import load_dotenv
from flask_cors import CORS
CORS(app)
load_dotenv()
import os
import json
app = Flask(__name__)
client=genai.Client(api_key=os.getenv("GENAI_API_KEY"))

@app.route('/')
def home():
    return redirect(url_for('welcome'))
@app.route('/welcome')
def welcome():
    return render_template('welcome.html')

@app.route('/chatp')
def chat_page():
    return render_template('chat.html')

@app.route('/get_response', methods=['POST'])
def chat():
    data = request.get_json()
    question = data.get('question')

    prompt =f"""
    you are MedInfo Chatbot, will give the accurate and precise information about any disease and basically designed to
    aware user about the disease. You will give the precise and 100% accurate information about disease by fetch only from 
    the WHO dataset and real trusted sources. 
    you response should be brief and clear in about 3 to 4 lines or few more if needed much
    1.Disease
    2.Precaution
    3.Symptoms
    your main task is to aware
    User Question:{question}
    """

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt)
    reply=response.candidates[0].content.parts[0].text
    return jsonify({"reply":reply})


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(port=port)