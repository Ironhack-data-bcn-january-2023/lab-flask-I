from flask import Flask, request, jsonify
import random
import sql_queries as sql2
import sql_connection as sql3



app = Flask (__name__)



@app.route("/")
def hello_world():
    return "Hello world!"

@app.route("/random/<therange>")
def random_number (therange):
    therange = int(therange)
    return str(random.randint(0, therange))

@app.route("/everything-employees")
def example ():
    return jsonify(sql2.get_everything())

@app.route("/table/<one_table>")
def table_ten (one_table):
    return jsonify(sql2.table_ten(one_table))

@app.route("/insert-into-employees", methods=["POST"])
def insert_by_passing_params ():

    id_ = request.args["id_"] # params.id_ = {}
    date = request.args["date"]
    name = request.args["name"] 
    fname = request.args["fname"] 
    gender = request.args["gender"] 
    date_2 = request.args["date_2"] 

    sql3.insert_params (id_, date, name, fname, gender, date_2)
    return "ok"

if __name__ == "__main__": #this prevents the moduel from being 
    # accidentally run when imported
    # makes sure its either module or script
    app.run(port=9000, debug=True)


