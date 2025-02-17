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