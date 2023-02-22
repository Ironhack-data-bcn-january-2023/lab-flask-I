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

@app.route("/insert-into-employees", methods=["POST"])
def insert_params_():
    emp_no = request.args['emp_no']
    birth_date = request.args['birth_date']
    first_name =request.args['first_name']
    last_name =request.args ['last_name']
    gender =request.args ['gender']
    hire_date = request.args['hire_date']
    
    sql.insert_params (emp_no, birth_date, first_name, last_name, gender, hire_date)
    return "Inserted!"

if __name__ == "__main__":
     app.run(port=7070, debug=True)
