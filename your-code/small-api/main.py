from flask import Flask, request, jsonify
import random

app = Flask(__name__)
@app.route("/", methods=["GET"])
def hello_this_works ():
    return f"Hello world!"

@app.route("/random-number", methods=["GET"])
def random_no():
    return str(random.randint(0,10))
app.run(port=9000, debug=True)