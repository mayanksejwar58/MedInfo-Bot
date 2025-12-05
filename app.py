from flask import Flask, render_template,request, jsonify
from google import genai
import json
app = Flask(__name__)
client=genai.Client(api_key='AIzaSyDmQB_ncrzoOMnSd9teArjafaWJnh0Kdyk')
@app.route('/')
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
    you are MedInfo Chatbot, who will give the exact information about the user question regarding any disease awareness 
    in about 2-3 line whenever user ask question. you just give first information about that disease and then symptoms 
    at last precautions 
    {question}
    """

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt)
    reply=response.candidates[0].content.parts[0].text
    return jsonify({"reply":reply})


if __name__ == '__main__':
    app.run(debug=True)
