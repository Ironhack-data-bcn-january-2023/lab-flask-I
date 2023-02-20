import sqlalchemy as alch
import os 
from dotenv import load_dotenv
import pandas as pd
from config.sql_connection import engine


def get_everything ():
    query = "SELECT * FROM  salaries LIMIT 10;"
    df = pd.read_sql_query(query, engine)
    return df.to_dict(orient="records")

def tbl_ten(tbl):
    query = f"SELECT * FROM {tbl} LIMIT 10;"
    df = pd.read_sql_query(query, engine)
    return df.to_dict(orient="records")