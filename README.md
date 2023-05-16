# Sample API App

SampleApi is the demo project.

The SampleApi runs across two containers:

- **api** - a Python REST API which serves data CURD operation
- **db** - a Postgres database that stores data

## Build and run in Docker Compose

The only requirement to build and run the app from source is Docker. Clone this repo and use Docker Compose to build all the images. You can use the new V2 Compose with `docker compose` or the classic `docker-compose` CLI:

-> update the server volumes in docker-compose.yml file according to the work dir.

```shell
docker compose up --build
```

Or you can pull pre-built images from Docker Hub using `docker compose pull`.

NOTE:
-> Below comments to be ran in the server CLI:
    * Run create_db.py using the command (python create_db.py)
    * Run create_table.py using the command (python create_table.py)
    * Run insert_data.py using the command (python insert_data.py) - update the folder_path according to the work dir.
