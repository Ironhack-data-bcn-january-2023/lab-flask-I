import pandas as pd
from sql_connection import engine

def get_everything():
    query = "SELECT * FROM salaries LIMIT 10;"
    df = pd.read_sql_query(query, engine)
    return df.to_dict(orient="records")

def tbl_tn(table):
    query = f"SELECT * FROM {table} LIMIT 10;"
    df= pd.read_sql_query(query, engine)
    return df.to_dict(orient= "records") 