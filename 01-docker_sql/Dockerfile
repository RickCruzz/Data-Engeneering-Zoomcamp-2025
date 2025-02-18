FROM python:3.9.1


RUN apt-get install wget
RUN pip install pandas SQLAlchemy psycopg2 pyarrow fastparquet

WORKDIR /app
COPY upload_data.py upload_data.p

ENTRYPOINT [ "python","upload_data.py" ]
