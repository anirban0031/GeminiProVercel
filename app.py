import requests,os
from flask import Flask, jsonify, request
from dotenv import load_dotenv

app = Flask(__name__)


description = {
    'Language-Model': 'gemini-pro',
    'version': 'v1beta',
    'language': 'python (flask)',
    'routes': ['/testrouter','/testrouter_a','/search/<typehere>']
}

@app.route("/")
def home():
    return description



@app.errorhandler(404)
def page_not_found(e):
    return jsonify({"status": 404, "message": "Not Found"}), 404

def call_api(text_var):

    load_dotenv()
    # Replace with your actual Google API key
    api_key = os.getenv('GOOGLE_API_KEY')

    # we can also define requested data and pass it through  "wordSchema"
    # wordSchema = {
    #     'type': 'object',
    #     'properties': {
    #         'Word': { 'type': 'string' },
    #         'Meaning': { 'type': 'string' },
    #         'Sentence': { 'type': 'string' }
    #     }
    # }

    url = "https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent?key=" + api_key

    headers = {
        "Content-Type": "application/json"
    }

    data = {
        "contents": [
            {
                "parts": [
                    {"text": text_var} #{"text": text_var +" "+ str(wordSchema)}
                ]
            }
        ]
    }

    response = requests.post(url, headers=headers, json=data)

    if response.status_code == 200:
        print(response.json())
    else:
        print("Error:", response.status_code, response.text)

    list_words_array=response.json()
    list_words=list_words_array["candidates"][0].get("content")["parts"][0]
    text_data = [list_words]
    
    return text_data
        
        

@app.route("/testrouter")
def testalp():
    return call_api("Give me 10 english words.")

@app.route("/testrouter_a")
def testalp_def():
    return call_api("Give me 10 english words with meaning.")

@app.route("/search/<typehere>")
def test(typehere):
    return call_api(typehere)

