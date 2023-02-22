
from flask import Flask, request, jsonify
import random
import requests
import tools.sql_queries as sql
import config.sql_connection as engine

app = Flask(__name__)
@app.route("/hello_world")
def hello_world():
    return f"Hello world!"

@app.route("/random")
def random_int():
    return str(random.randint(0, 10))


@app.route("/everything-employees")
def example():
    return jsonify(sql.get_everything())

@app.route("/table/<tbl>")
def tbl_ten(tbl):
    return jsonify(sql.tbl_ten(tbl))


if __name__ == "__main__":
    app.run(port=7070, debug=True)



