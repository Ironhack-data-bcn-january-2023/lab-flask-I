from flask import Flask, request, jsonify
import random
import sql_connection as engine
import sql_queries as sql


app = Flask(__name__)
@app.route("/", methods=["GET"])
def hello_this_works ():
    return f"Hello world!"

@app.route("/random")
def random_no():
    return str(random.randint(0,10))

@app.route("/everything-employees")
def example():
    return jsonify(sql.get_everything())

@app.route("/table/<table>")
def table_ten(table):
    return jsonify(sql.tbl_tn(table))

if __name__ == "__main__":
     app.run(port=7070, debug=False)




