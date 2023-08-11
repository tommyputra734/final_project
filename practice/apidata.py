#%%
import requests
import json
import pandas as pd
from pandas import json_normalize
from pathlib import Path
import psycopg2
from sqlalchemy import create_engine

# %%
response_API = requests.get('http://103.150.197.96:5005//api/v1/rekapitulasi_v2/jabar/harian')
print(response_API.status_code)
# %%
data = response_API.text
print(data)
parse_json = json.loads(data)
print(parse_json)
# %%
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
# %%
test = flatten_json(parse_json)
for k in test:
    print(k)
# df = pd.DataFrame.from_dict(flatten_json(parse_json), orient='index')
# %%
# df = pd.DataFrame.from_dict(flatten_json(parse_json),orient='index')
# %%
df = pd.json_normalize(flatten_json(parse_json), record_path='dataconten')
# print(df)
df.columns.values.tolist()
# df.to_csv(r'C:\Users\Babatunde\Desktop\Digital_Skola_File\Final Project\practice\data\exampledata5.csv', index=False, header=True)
# %%
pd.read_csv(r'C:\Users\Babatunde\Desktop\Digital_Skola_File\Final Project\practice\data\exampledata.csv')
# %%
conn = psycopg2.connect(host='localhost',
                        port='5432',
                        dbname='postgres',
                        user='postgres',
                        password='forward421q')

conn.autocommit = True

cur = conn.cursor()
#%%
cur.execute("""
            CREATE TABLE latihan_airflow (
                id serial PRIMARY KEY,
                CLOSECONTACT bigint,
                CONFIRMATION bigint,
                PROBABLE bigint,
                SUSPECT bigint,
                closecontact_dikarantina bigint,
                closecontact_discarded bigint,
                closecontact_meninggal bigint,
                confirmation_meninggal bigint,
                confirmation_sembuh bigint,
                kode_kab text,
                kode_prov text,
                nama_kab text,
                nama_prov text,
                probable_diisolasi bigint,
                probable_discarded bigint,
                probable_meninggal bigint,
                suspect_diisolasi bigint,
                suspect_discarded bigint,
                suspect_meninggal bigint,
                tanggal text
            )
            """)
#%%
engine = create_engine('postgresql://postgres@172.22.240.1:5432/postgres')
df.to_sql('airflow_test', con=engine, if_exists='replace')