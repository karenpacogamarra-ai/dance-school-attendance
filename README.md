# Dance School Attendance

In this project, we track attendance of the students for each dance class.

> Early stage project: only student and dance-class endpoints exist so far. Attendance tracking itself is not yet implemented, and the API currently keeps data in memory (it resets on every restart) — the database service below is provisioned but not yet wired up.

## Requirements

- [uv](https://docs.astral.sh/uv/) (for running locally) **or** Docker + Docker Compose (for running in containers)

## Option A: Run locally with uv

```
uv venv
source .venv/bin/activate
uv run fastapi dev src/main.py
```

The API will be available at http://localhost:8000, with interactive docs at http://localhost:8000/docs.

## Option B: Run with Docker Compose

This spins up the FastAPI app plus a MariaDB database.

```
docker compose up --build
```

Or, using the provided Makefile:

```
make up
```

The API will be available at http://localhost:8000. Source code under `src/` is mounted into the container, so `fastapi dev`'s auto-reload picks up local changes without rebuilding the image.

### Makefile targets

| Target        | Description                                  |
|---------------|-----------------------------------------------|
| `make up`     | Build (if needed) and start all services       |
| `make up-d`   | Same as `up`, but detached (runs in background) |
| `make down`   | Stop and remove containers                     |
| `make logs`   | Follow logs from all services                  |
| `make ps`     | Show status of running services                |
| `make restart`| Restart the API service                        |
| `make clean`  | Stop containers and remove volumes (⚠️ deletes DB data) |

### Services

- **dance-api** — the FastAPI app, built from the local `Dockerfile`, exposed on port `8000`.
- **db** — MariaDB 11.4, exposed on port `3306`, with credentials defined in `docker-compose.yml` and data persisted in the `mariadb_data` volume.

## Project structure

```
src/
├── main.py         # FastAPI entrypoint, mounts routers
├── controller/      # APIRouters, one per domain entity
├── service/         # business logic
├── dto/             # pydantic request/response models
└── repository/       # data access layer (in-memory for now)
```

There are no lint or test commands configured yet.
