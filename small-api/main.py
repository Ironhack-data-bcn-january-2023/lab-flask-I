from flask import Flask, request, jsonify
import random

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "Hello world!"

@app.route("/multiply/<num1>/<num2>")
def speak(num1,num2):
    result=int(num1)*int(num2)
    return f"{num1} times {num2} is {result}"

@app.route("/random-number")
def random_int():
    return str(random.randint(0, 10))


if __name__ == "__main__":
    app.run(port=7070, debug=True)
