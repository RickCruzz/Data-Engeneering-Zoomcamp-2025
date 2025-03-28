#!/usr/bin/env python
# coding: utf-8

# In[2]:

import argparse

import pyspark
from pyspark.sql import SparkSession
from pyspark.sql import functions as F


# In[3]:

parser = argparse.ArgumentParser(description="Configs for Spark Job")
# User, Password, Host, Database Name, Table Name and URL of the csv

parser.add_argument("--input_green", required=True, help="Green Location")
parser.add_argument("--input_yellow", required=True, help="Yellow Location")
parser.add_argument("--output", required=True, help="Output Location")

args = parser.parse_args()

input_green = args.input_green
input_yellow = args.input_yellow
output = args.output


spark = SparkSession.builder \
    .appName('test') \
    .getOrCreate()

spark.conf.set('temporaryGcsBucket','dataproc-temp-us-central1-751623831627-yc8hulov')


# In[4]:


df_green = spark.read.parquet(input_green)


# In[5]:


#df_green.show(10,False)


# In[6]:


df_yellow = spark.read.parquet(input_yellow)


# In[7]:


#df_yellow.show(5,False)


# In[8]:


df_green = df_green \
    .withColumnRenamed('lpep_pickup_datetime','pickup_datetime') \
    .withColumnRenamed('lpep_dropoff_datetime','dropoff_datetime')


# In[9]:


df_yellow = df_yellow \
    .withColumnRenamed('tpep_pickup_datetime','pickup_datetime') \
    .withColumnRenamed('tpep_dropoff_datetime','dropoff_datetime')


# In[10]:


#Selecting all columns for both
common_columns = []
yellow_columns = set(df_yellow.columns)
for col in df_green.columns:
    if col in yellow_columns:
        common_columns.append(col)


# In[11]:


df_green_sel = df_green.select(common_columns) \
    .withColumn('service_type', F.lit('green'))


# In[12]:


df_yellow_sel = df_yellow.select(common_columns) \
    .withColumn('service_type', F.lit('yellow'))


# In[13]:


df_trips_data = df_green_sel.unionAll(df_yellow_sel)


# In[14]:


df_trips_data.groupBy('service_type').count().show()


# In[15]:


df_trips_data.createOrReplaceTempView('trips_data')


# In[16]:


#spark.sql("""
#Select service_type, count(1) as count
#from trips_data
#group by service_type
#""").show()


# In[17]:


df_result = spark.sql("""
    select 
    -- Revenue grouping 
    PULocationID as revenue_zone,
    date_trunc('month', cast(pickup_datetime as TIMESTAMP)) as revenue_month,
    service_type, 

    -- Revenue calculation 
    sum(fare_amount) as revenue_monthly_fare,
    sum(extra) as revenue_monthly_extra,
    sum(mta_tax) as revenue_monthly_mta_tax,
    sum(tip_amount) as revenue_monthly_tip_amount,
    sum(tolls_amount) as revenue_monthly_tolls_amount,
    sum(improvement_surcharge) as revenue_monthly_improvement_surcharge,
    sum(total_amount) as revenue_monthly_total_amount,

    -- Additional calculations
    avg(passenger_count) as avg_monthly_passenger_count,
    avg(trip_distance) as avg_monthly_trip_distance

    from trips_data
    group by revenue_zone, revenue_month, service_type
""")


# In[18]:


#df_result.show(5)


# In[56]:


df_result.write.format('bigquery') \
    .option('table', output) \
    .save()


