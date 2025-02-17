## Docker
- A tool for containerization and making things run in Isolation.
- Containers mean Images.
- Containers can be a Data Pipeline where you can use multiple tools or requirements Example: Container A [Ubuntu 20.04, Python 3.9, Pandas, Postgres] | Container B [Database (Postgres)] | Container C [PgAdmin] Thats Connects to Container A and B
### Why?
- Local Experiments -> Run as tests and understood tasks
- Integration tests (CI/CD) -> Generate Images and update code
- Spark (Pré-Requistes)
- Serverless (AWS Lambda, Google Functions)
- Reproducibility -> Export to different scenarios and Making sure everything don't just run on "my machine"

### Dockerfile
- Instructions for what your Image will be depending on like Pandas, Requests or other librarys if you want to create a python like image.


### Main Commands
- docker run -it "IMAGE_NAME" (interactive mode)
- docker ps (Shows all running images)

- Running postgres image:
```
docker run -it \
  -e POSTGRES_USER="root" \
  -e POSTGRES_PASSWORD="root" \
  -e POSTGRES_DB="ny_taxi" \
  -v $(pwd)/ny_taxi_postgres_data:/var/lib/postgresql/data \
  -p 5432:5432 \
  postgres:13
``` 

- PgAdmin image start:
```
docker run -it \
  -e PGADMIN_DEFAULT_EMAIL="admin@admin.com" \
  -e PGADMIN_DEFAULT_PASSWORD="root" \
  -p 8080:80 \
  dpage/pgadmin4
``` 

- Remember to add the connection between the Docker images.
```
docker network create pg-network
```

- Adding Network Connection
```
docker run -it \
  -e POSTGRES_USER="root" \
  -e POSTGRES_PASSWORD="root" \
  -e POSTGRES_DB="ny_taxi" \
  -v $(pwd)/ny_taxi_postgres_data:/var/lib/postgresql/data \
  --network=pg-network \
  --name pg-database \
  -p 5432:5432 \
  postgres:13

#PGADMIN

docker run -it \
  -e PGADMIN_DEFAULT_EMAIL="admin@admin.com" \
  -e PGADMIN_DEFAULT_PASSWORD="root" \
  -p 8080:80 \
  --network=pg-network \
  --name pgadmin \
  dpage/pgadmin4
``` 
- Maybe you need to remove the older Container try with: ``` docker rm <container_name_or_id> ``` 