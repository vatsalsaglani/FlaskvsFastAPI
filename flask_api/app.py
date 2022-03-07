from flask import Flask, jsonify, request
from flask_cors import CORS
from util import multiply_util

app = Flask(__name__)


@app.route("/api/multiply", methods=["GET"])
def api_multiply():
    ans = multiply_util(5)
    return jsonify({"message": "Hello"})


if __name__ == "__main__":
    app.run(port=5500, debug=True)
