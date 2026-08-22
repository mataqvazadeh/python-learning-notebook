# Sample Projects and Files Index

This index covers every file currently stored under `sessions/session*/samples/`.

Some early samples are small single-file classroom examples. Newer Docker samples are structured mini-projects with their own `Dockerfile` or `compose.yaml`.

## Overview

| Session | Focus | File count |
|---------|-------|------------|
| 02 | Python control-flow samples | 4 |
| 03 | Functions and modules samples | 7 |
| 04 | File handling, exceptions, and sample assets | 13 |
| 05 | Dictionary/type samples | 1 |
| 06 | Functions, recursion, and sorting samples | 4 |
| 07 | Iterators, generators, decorators samples | 3 |
| 09 | OOP basics samples | 5 |
| 10 | OOP/inheritance samples | 9 |
| 11 | Big-O, data structures, dataclass samples | 6 |
| 15 | Advanced Python samples | 3 |
| 17 | SQL samples | 3 |
| 45 | Docker and Docker Compose samples | 26 |
| 46 | Dockerized Django deployment helper scripts | 1 |

## Complete Sample File Inventory

### session02 — Python control-flow samples

- `sessions/session02/samples/age.py`
- `sessions/session02/samples/break.py`
- `sessions/session02/samples/conditional.py`
- `sessions/session02/samples/loop.py`

### session03 — Functions and modules samples

- `sessions/session03/samples/func-2.py`
- `sessions/session03/samples/func-3.py`
- `sessions/session03/samples/func.py`
- `sessions/session03/samples/list_printer.py`
- `sessions/session03/samples/modules.py`
- `sessions/session03/samples/print_list.py`
- `sessions/session03/samples/w01-cw05.py`

### session04 — File handling, exceptions, and sample assets

- `sessions/session04/samples/exceptions.py`
- `sessions/session04/samples/hw.py`
- `sessions/session04/samples/python.jpeg`
- `sessions/session04/samples/read-file.py`
- `sessions/session04/samples/text01.txt`
- `sessions/session04/samples/text02.txt`
- `sessions/session04/samples/text03.txt`
- `sessions/session04/samples/text04.txt`
- `sessions/session04/samples/text05.txt`
- `sessions/session04/samples/text06.txt`
- `sessions/session04/samples/text07.txt`
- `sessions/session04/samples/text_root.txt`
- `sessions/session04/samples/write-file.py`

### session05 — Dictionary/type samples

- `sessions/session05/samples/dict.py`

### session06 — Functions, recursion, and sorting samples

- `sessions/session06/samples/adder.py`
- `sessions/session06/samples/functions.py`
- `sessions/session06/samples/merge-sort.py`
- `sessions/session06/samples/recursive.py`

### session07 — Iterators, generators, decorators samples

- `sessions/session07/samples/decorators.py`
- `sessions/session07/samples/generators.py`
- `sessions/session07/samples/iterators.py`

### session09 — OOP basics samples

- `sessions/session09/samples/animal-class.py`
- `sessions/session09/samples/classes.py`
- `sessions/session09/samples/person.py`
- `sessions/session09/samples/wallet.py`
- `sessions/session09/samples/wallet_usage.py`

### session10 — OOP/inheritance samples

- `sessions/session10/samples/ball.py`
- `sessions/session10/samples/diamond.py`
- `sessions/session10/samples/encapsulation.py`
- `sessions/session10/samples/file-handler.py`
- `sessions/session10/samples/hovercraft.py`
- `sessions/session10/samples/lifecycle.py`
- `sessions/session10/samples/mixin.py`
- `sessions/session10/samples/shape.py`
- `sessions/session10/samples/todolist.py`

### session11 — Big-O, data structures, dataclass samples

- `sessions/session11/samples/bigo.py`
- `sessions/session11/samples/dataclass.py`
- `sessions/session11/samples/main.py`
- `sessions/session11/samples/my_queue.py`
- `sessions/session11/samples/stack.py`
- `sessions/session11/samples/two-sum.py`

### session15 — Advanced Python samples

- `sessions/session15/samples/context-manager.py`
- `sessions/session15/samples/iterators.py`
- `sessions/session15/samples/scopes.py`

### session17 — SQL samples

- `sessions/session17/samples/create_table.sql`
- `sessions/session17/samples/cross_join.sql`
- `sessions/session17/samples/simple_join.sql`

### session45 — Docker and Docker Compose samples

- `sessions/session45/samples/compose_postgres_logger/.dockerignore`
- `sessions/session45/samples/compose_postgres_logger/Dockerfile`
- `sessions/session45/samples/compose_postgres_logger/compose.yaml`
- `sessions/session45/samples/compose_postgres_logger/logger.py`
- `sessions/session45/samples/compose_postgres_logger/requirements.txt`
- `sessions/session45/samples/compose_redis_logger/.dockerignore`
- `sessions/session45/samples/compose_redis_logger/Dockerfile`
- `sessions/session45/samples/compose_redis_logger/compose.yaml`
- `sessions/session45/samples/compose_redis_logger/logger.py`
- `sessions/session45/samples/compose_redis_logger/requirements.txt`
- `sessions/session45/samples/config_reader/.dockerignore`
- `sessions/session45/samples/config_reader/Dockerfile`
- `sessions/session45/samples/config_reader/config.json`
- `sessions/session45/samples/config_reader/read_config.py`
- `sessions/session45/samples/greeting_app/.dockerignore`
- `sessions/session45/samples/greeting_app/Dockerfile`
- `sessions/session45/samples/greeting_app/greet.py`
- `sessions/session45/samples/looping_worker/.dockerignore`
- `sessions/session45/samples/looping_worker/Dockerfile`
- `sessions/session45/samples/looping_worker/worker.py`
- `sessions/session45/samples/report_writer/.dockerignore`
- `sessions/session45/samples/report_writer/Dockerfile`
- `sessions/session45/samples/report_writer/write_report.py`
- `sessions/session45/samples/simple_http/.dockerignore`
- `sessions/session45/samples/simple_http/Dockerfile`
- `sessions/session45/samples/simple_http/server.py`

### session46 — Dockerized Django deployment helper scripts

- `sessions/session46/samples/entrypoint.sh`

## Structured Docker Samples

| Path | Used by | Purpose |
|------|---------|---------|
| `sessions/session45/samples/greeting_app/` | `S45P02-DockerfileImages.ipynb` | Simple `CMD` example and command override |
| `sessions/session45/samples/config_reader/` | `S45P02-DockerfileImages.ipynb` | Copying multiple files into a Docker image |
| `sessions/session45/samples/report_writer/` | `S45P02-DockerfileImages.ipynb` | Writing files and introducing bind mounts/volumes |
| `sessions/session45/samples/looping_worker/` | `S45P02-DockerfileImages.ipynb` | Detached containers, logs, stop/remove lifecycle |
| `sessions/session45/samples/simple_http/` | `S45P02-DockerfileImages.ipynb` | Request/response and port mapping |
| `sessions/session45/samples/compose_redis_logger/` | `S45P03-DockerCompose.ipynb` | Multi-container Compose project with Python + Redis |
| `sessions/session45/samples/compose_postgres_logger/` | `S45P03-DockerCompose.ipynb` | Optional Compose exercise with Python + PostgreSQL + volume |
| `sessions/session46/samples/entrypoint.sh` | `S46P02-DockerizedDeployment.ipynb` | Startup wrapper for waiting on PostgreSQL, migrations, and static files |

## How to Run Samples

Many early samples are regular Python scripts:

```bash
python3 sessions/session02/samples/loop.py
```

Some SQL samples are intended to be opened or executed from a PostgreSQL client, depending on the lesson.

Dockerfile samples are run from their own directory:

```bash
cd sessions/session45/samples/greeting_app
docker build -t greeting_app .
docker run greeting_app
```

Compose samples are also run from their own directory:

```bash
cd sessions/session45/samples/compose_redis_logger
docker compose up --build
```

Check the related notebook for the expected commands, output, and cleanup steps.

## Maintenance Note

When adding a new `sessions/session*/samples/` file or mini-project, update this index so GitHub visitors can find runnable examples without browsing every session folder.
