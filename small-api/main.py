from flask import Flask, request, jsonify
import random
import sql_queries as sql
import requests

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

# POST THINGS INTO SQL
@app.route("/insert/<the_table>/<d_id>/<name>", methods = ["POST"])
def insert_into_table (the_table, d_id, name):
    sql.insert_one(the_table, d_id, name)
    return "Inserted!"

@app.route("/insert-into-employees", methods=["POST"])
def insert_by_passing_params ():

    emp_no = request.args["emp_no"] 
    birth_date = request.args["birth_date"]
    first_name = request.args["first_name"] 
    last_name = request.args["last_name"] 
    gender = request.args["gender"] 
    hire_date = request.args["hire_date"] 

    sql.insert_params (emp_no, birth_date, first_name, last_name, gender, hire_date)
    return "ok"

@app.route("/insert-department", methods=["POST"])
def insert_depart ():

    dept_no = request.args["dept_no"] 
    dept_name = request.args["dept_name"]

    sql.insert_dept (dept_no, dept_name)
    return "ok"

if __name__ == "__main__":
     app.run(port=7070, debug=True)

