import flask
from flask import Flask, request, jsonify
import random

# your code here
app = Flask(__name__)



@app.route("/")
def hello_world ():
    return f"Hello World"

@app.route("/random-number")
def random_int():
     return str(random.randint(0, 10))


if __name__ == "__main__":
     app.run(port=8123, debug= True)