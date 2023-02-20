import requests
import random
from flask import Flask, request, jsonify
app = Flask(__name__)
@app.route("/hello_world")
def hello_world():
    return f"Hello world!"

@app.route("/random")
def random_int():
    return str(random.randint(0, 10))

if __name__ == "__main__":
    app.run(port=7070, debug=True)