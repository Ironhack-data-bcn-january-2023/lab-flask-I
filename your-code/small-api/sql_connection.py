import sqlalchemy as alch
import os 
from dotenv import load_dotenv
import pandas as pd


# Loading env variables
load_dotenv()
password = os.getenv("password_sql")

# Connection to database
dbName = "employees"
connectionData=f"mysql+pymysql://root:{password}@localhost/{dbName}"
engine = alch.create_engine(connectionData)




def insert_params (id_, date, name, fname, gender, date_2):
    query = f"""
    INSERT INTO employees
    VALUES ("{id_}", "{date}", "{name}", "{fname}", "{gender}", "{date_2}");
    """
    engine.execute(query)

