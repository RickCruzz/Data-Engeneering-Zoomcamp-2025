## Module 5 - Batch Processing

### What is Batch processing?
Takes some chunks of data, usually Daily data.

### Technologies
- Python Scripts
- SQL
- Spark
- Flink

### Advantages of Batch
- Easy to Manage
- Retry is Safe
- Scalability

### Disavantage
- Delay of availability of data (if you want closer data)

### Spark 

### When?
When is in a Datalake (s3/GCS), Spark will put the data, process and put back in the Datalake

### Configuring into Machine:
(https://github.com/DataTalksClub/data-engineering-zoomcamp/tree/50377191493a29d49f181e4f4081f29655bbd6f3/05-batch/setup)
export PYTHONPATH="${SPARK_HOME}/python/:$PYTHONPATH"
export PYTHONPATH="${SPARK_HOME}/python/lib/py4j-0.10.9.5-src.zip:$PYTHONPATH"



### Spark Internals

REAL SCENARIO

From your machine you can wrote code in Python and we have a cluster
Inside this cluster we have a [Master]
My Machine Submit package to Master.
A cluster can have multiple machines to Execute the jobs submitted.(Executors)

Machine -> Master -> Executor

### Running locally vs Running With Local Cluster

URL="spark://de-zoomcamp.us-central1-c.c.zoomcamp-2025-451318.internal:7077"

spark-submit \
    --master="${URL}" \
    10_SparkSQL_Local.py \
        --input_green=data/pq/green/2021/*/ \
        --input_yellow=data/pq/yellow/2021/*/ \
        --output=data/report/report-2021


python 10_SparkSQL_Local.py \
    --input_green=data/pq/green/2020/*/ \
    --input_yellow=data/pq/yellow/2020/*/ \
    --output=data/report/report-2020

### Last Chapter - DataProc

Submiting via Terminal

gcloud dataproc jobs submit pyspark \
    --cluster=de-zoomcamp-2025-cluster-hc \
    --region=us-central1 \
    gs://ny-taxis-bucket-zoomcamp-2025/code/10_sparksql.py \
    -- \
        --input_green=gs://ny-taxis-bucket-zoomcamp-2025/pq/green/2021/* \
        --input_yellow=gs://ny-taxis-bucket-zoomcamp-2025/pq/yellow/2021/* \
        --output=gs://ny-taxis-bucket-zoomcamp-2025/reports/2021

### Saving in BQ

gcloud dataproc jobs submit pyspark \
    --cluster=de-zoomcamp-2025-cluster-hc \
    --region=us-central1 \
    gs://ny-taxis-bucket-zoomcamp-2025/code/11_sparksql_bq.py \
    -- \
        --input_green=gs://ny-taxis-bucket-zoomcamp-2025/pq/green/2020/* \
        --input_yellow=gs://ny-taxis-bucket-zoomcamp-2025/pq/yellow/2020/* \
        --output=ny_taxis_zoomcamp_2025.report_2020


