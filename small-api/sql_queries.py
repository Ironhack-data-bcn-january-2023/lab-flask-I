import pandas as pd
from sql_connection import engine

def get_everything():
    query = f"SELECT * FROM salaries  LIMIT 10;"
    df = pd.read_sql_query(query, engine)
    return df.to_dict(orient="records")

def table_ten(one_table):
    query = f"SELECT * FROM {one_table}  LIMIT 10;"
    df = pd.read_sql_query(query, engine)
    return df.to_dict(orient="records")

def insert_params (emp_no, birth_date, first_name, last_name, gender, hire_date):
    query = f"""
    INSERT INTO employees
    VALUES ("{emp_no}", "{birth_date}", "{first_name}", "{last_name}", "{gender}", "{hire_date}");
    """
    engine.execute(query)

def insert_dept (dept_no, dept_name):
    query = f"""
    INSERT INTO departments
    VALUES ("{dept_no}", "{dept_name}");
    """
    engine.execute(query)