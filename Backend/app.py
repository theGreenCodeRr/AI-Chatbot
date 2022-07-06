from flask import Flask, request, jsonify
from chat import get_response
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.post('/predict')
def predict():
    text = request.get_json().get("massage")
    response = get_response(text)
    massage = {"answer": response}
    return jsonify(massage)


if __name__ == '__main__':
    app.run(debug=True)
    