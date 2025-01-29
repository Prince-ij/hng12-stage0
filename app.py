#!/usr/bin/python3
from flask import Flask, jsonify
from datetime import datetime
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/", methods=["GET"])
def home():
    response = {
        "email": "aminuibrahimthefifth@gmail.com",
        "current_datetime": datetime.utcnow().replace(microsecond=0).isoformat() + "Z",
        "github_url": "https://github.com/Prince-ij/hng12-stage0"
    }
    return jsonify(response), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
