import sqlalchemy as alch
import os 
from dotenv import load_dotenv
import pandas as pd

#load env vars
load_dotenv()
password = os.getenv('password')

#connecting to db
dbName = 'employees'
connectionData = f'mysql+pymysql://root:{password}@localhost/{dbName}'
engine = alch.create_engine(connectionData)