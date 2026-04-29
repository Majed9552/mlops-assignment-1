from flask import Flask, jsonify, request
app = Flask(__name__)

@app.route('/')
def home():
    return '<h1>MLOps Assignment 1: Flask ML App</h1>'

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    return jsonify({'prediction': 'success', 'status': 200})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
