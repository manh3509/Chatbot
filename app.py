from typing import Text
from  flask import Flask, render_template,redirect,jsonify,request
from flask_cors import CORS

from chat import get_response

app = Flask(__name__)
CORS(app)

@app.route('/', methods=['GET'])
def index_get():
    return render_template('base.html')

@app.post("/predict")
def predict():
    text = request.get_json().get("message")
    #TODO: check if text is valid
    response = get_response(text)
    message = {"answer": response}
    return jsonify(message)


if __name__ == "__main__":
    app.run(host='0.0.0.0',port='8080')