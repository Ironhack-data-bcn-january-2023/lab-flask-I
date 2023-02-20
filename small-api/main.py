from flask import Flask, request, jsonify
import random

app = Flask(__name__)

@app.route("/random/<therange>")
def random_int(therange):
    therange = int(therange)
    return str(random.randint(0, therange)) 

if __name__ == "__main__":
     app.run(port=7070, debug=False)