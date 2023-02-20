import pandas as pd
from tools.sql_connection import engine

def get_everything_table ():
    query = f"SELECT * FROM salaries LIMIT 10;"
    df = pd.read_sql_query(query, engine)
    return df.to_dict(orient="records")

def table_ten (table_q):
    query = f"SELECT * FROM  {table_q} LIMIT 10;"
    df = pd.read_sql_query(query, engine)
    return df.to_dict(orient="records")