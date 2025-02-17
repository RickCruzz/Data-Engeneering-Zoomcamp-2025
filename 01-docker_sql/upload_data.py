#%%
import pandas as pd
#check version
pd.__version__

#%%
# Reading data
df =  pd.read_parquet("yellow_tripdata_2024-01.parquet")

#%%
# Connecting to postgres
from sqlalchemy import create_engine
engine = create_engine("postgresql://root:root@localhost:5432/ny_taxi")
engine.connect()

#%%
#Getting the schema / Create table
print(pd.io.sql.get_schema(df, name="yellow_taxi_data", con=engine))

#%%
#Now because the file is already a parquet we dont need to use a iterator as described in course
#Creating a interator forcing to have 100.000 rows per iteration
#df_iter =  pd.read_csv("yellow_tripdata_2021-01.csv", iterator=True, chunksize=100000)

#df = next(df_iter)

#df.tpep_pickup_datetime = pd.to_datetime(df.tpep_pickup_datetime)
#df.tpep_dropoff_datetime = pd.to_datetime(df.tpep_dropoff_datetime)

#Forcing the creation of the table using head(n=0) And do the FIRST insert
#df.head(n=0).to_sql(name='yellow_taxi_data', con=engine, if_exists='replace')
#df.to_sql(name='yellow_taxi_data', con=engine, if_exists='append')

#Inserting the rest on a Loop
#from time import time
#while True:
#    t_start = time()
#    df = next(df_iter)
#    df.tpep_pickup_datetime = pd.to_datetime(df.tpep_pickup_datetime)
#    df.tpep_dropoff_datetime = pd.to_datetime(df.tpep_dropoff_datetime)
#    df.to_sql(name='yellow_taxi_data', con=engine, if_exists='append')
#    t_end = time()
#    print("Inserted another chunk, took %.3f Second' %(t_end - t_start))
#    

#%%
# WORKING WITH PARQUET:

#Forcing the creation of the table using head
df.head(n=0).to_sql(name='yellow_taxi_data', con=engine, if_exists='replace')

#%%
# Append the Parquet file to database
df.to_sql(name='yellow_taxi_data', con=engine, if_exists='append')


