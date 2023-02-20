from flask import Flask, jsonify, request
import random


app = Flask(__name__)


@app.route("/")
def hello_world():
    return "Hello world!"

@app.route("/random-number")
def random_number ():
    return str(random.randint(0, 10))

if __name__ == "__main__":
     app.run(port=7070, debug=False)
