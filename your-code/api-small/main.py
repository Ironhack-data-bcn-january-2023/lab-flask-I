from flask import Flask, request, jsonify
import random 
import tools.sql_queries as sql

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World'

@app.route("/random")
def random_int():
    return str(random.randint(0, 10))

@app.route('/everything-employees')
def example():
    return jsonify(sql.get_everything())

@app.route('/table/<one_table>')
def table(one_table):
    return jsonify(sql.table_ten(one_table))


app.run(port=9000, debug=True)