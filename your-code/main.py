from flask import Flask, request, jsonify

import random

app = Flask(__name__)


@app.route("/hello-world")
def hello ():
    return f"Hello world!"


@app.route("/random/<therange>")
def random_number (therange):
    therange = int(therange)
    return str(random.randint(0, therange))


app.run(port=51814 , debug=True)