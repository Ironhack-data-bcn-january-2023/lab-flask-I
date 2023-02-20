from flask import Flask, request, jsonify
import random



app = Flask (__name__)

@app.route("/")
def hello_world():
    return "Hello world!"

@app.route("/random/<therange>")
def random_number (therange):
    therange = int(therange)
    return str(random.randint(0, therange))

if __name__ == "__main__": #this prevents the moduel from being 
    # accidentally run when imported
    # makes sure its either module or script
    app.run(port=9000, debug=True)

