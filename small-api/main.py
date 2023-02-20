from flask import Flask, request, jsonify
import random
import sql_queries as sql

app = Flask(__name__)

@app.route("/random/<therange>")
def random_int(therange):
    therange = int(therange)
    return str(random.randint(0, therange)) 

@app.route("/everything-employees")
def example ():
    return jsonify(sql.get_everything())

@app.route("/table/<one_table>")
def table (one_table):
    return jsonify(sql.table_ten(one_table))

if __name__ == "__main__":
     app.run(port=7070, debug=True)

