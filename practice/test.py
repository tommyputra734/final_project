import requests
import json
import pandas as pd
from pandas import json_normalize
from pathlib import Path
import psycopg2
from sqlalchemy import create_engine

response_API = requests.get('http://103.150.197.96:5005//api/v1/rekapitulasi_v2/jabar/harian')
data = response_API.text
parse_json = json.loads(data)

def flatten_json(json):
    dict1 = {}  
    def flatten(i, name=''):     
        if type(i) is dict:
         for a in i:
             flatten(i[a], name + a + '')
        else:
            dict1[name[:-1]] = i  
    flatten(json)
    return dict1

df = pd.json_normalize(flatten_json(parse_json), record_path='dataconten')
df.to_csv(r'C:\Users\Babatunde\Desktop\Digital_Skola_File\Final Project\practice\data\exampledata5.csv', index=False, header=True)

conn = psycopg2.connect(host='172.22.240.1',
                        port='5432',
                        dbname='postgres',
                        user='postgres',
                        password='forward421q')

conn.autocommit = True

cur = conn.cursor()

engine = create_engine('postgresql://postgres@172.22.240.1:5432/postgres')
df.to_sql('airflow_test', con=engine, if_exists='replace')