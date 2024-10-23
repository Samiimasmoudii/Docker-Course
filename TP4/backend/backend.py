from flask import Flask, jsonify
from flask_cors import CORS
import time

app = Flask(__name__)
CORS(app)  # This will allow cross-origin requests

@app.route('/Hello')
def hello():
    time.sleep(1)
    return jsonify({"message": "Hello from Flask backend!"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
