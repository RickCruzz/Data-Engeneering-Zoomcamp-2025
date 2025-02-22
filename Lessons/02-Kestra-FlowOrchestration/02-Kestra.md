## Workflow Orchestration with Kestra

### Resources
- [Quickstart Guide](https://go.kestra.io/de-zoomcamp/quickstart)
- [Install Kestra with Docker Compose](https://go.kestra.io/de-zoomcamp/docker-compose)
- [Tutorial](https://go.kestra.io/de-zoomcamp/tutorial)
- [What is an Orchestrator?](https://go.kestra.io/de-zoomcamp/what-is-an-orchestrator)

### Tips
- Namespace -> Folder/workspace

### Workflows
In the workflow Folder contain some files that can be imported into Any Namespace in Kestra

    - 01-local-kestra.yaml - Workflow to run using the Docker-Compose infrastructure
    - 02-gcp-kv.yaml - Workflow to Help to setup some parameters - ADD GCP_CREDS with the json from your Service Account
    - 03-gcp-setup.yaml - Workflow to Setup the Bucket + BigQuery Dataset
    - 04-gcp-taxi.yaml - Workflow Similar to the local-kestra but without the Schedule part