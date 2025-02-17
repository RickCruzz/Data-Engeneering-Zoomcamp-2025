import os
import pandas as pd
from time import time
from sqlalchemy import create_engine
import argparse

def main(params):
    t_start = time()
    user = params.user
    password = params.password
    host = params.host
    port = params.port
    db = params.db
    table_name = params.table_name
    url = params.url
    
    parquet_name = "output.parquet"
    #Download the PARQUET file
    os.system(f"wget {url} -O {parquet_name}")


    engine = create_engine(f"postgresql://{user}:{password}@{host}:{port}/{db}")
    df = pd.read_parquet(parquet_name)
    
    #Forcing the creation of the table using head
    df.head(n=0).to_sql(name=table_name, con=engine, if_exists='replace')

    # Append the Parquet file to database
    df.to_sql(name=table_name, con=engine, if_exists='append')
    t_end = time()
    print("Data Inserted Sucessfully, at took %.3f seconds" % (t_end - t_start))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Ingest PARQUET Files to Postgres")
    # User, Password, Host, Database Name, Table Name and URL of the csv

    parser.add_argument("--user", help="user name for postgres")
    parser.add_argument("--password", help="password for postgres")
    parser.add_argument("--host", help="host for postgres")
    parser.add_argument("--port", help="port for postgres")
    parser.add_argument("--db", help="database name for postgres")
    parser.add_argument("--table_name", help="name of the table to Insert")
    parser.add_argument("--url", help="url of the PARQUET file")

    args = parser.parse_args()
    main(args)


