# Sample Projects and Files Index

This index covers every file currently stored under `session*/samples/`.

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

## Complete Sample File Inventory

### session02 — Python control-flow samples

- `session02/samples/age.py`
- `session02/samples/break.py`
- `session02/samples/conditional.py`
- `session02/samples/loop.py`

### session03 — Functions and modules samples

- `session03/samples/func-2.py`
- `session03/samples/func-3.py`
- `session03/samples/func.py`
- `session03/samples/list_printer.py`
- `session03/samples/modules.py`
- `session03/samples/print_list.py`
- `session03/samples/w01-cw05.py`

### session04 — File handling, exceptions, and sample assets

- `session04/samples/exceptions.py`
- `session04/samples/hw.py`
- `session04/samples/python.jpeg`
- `session04/samples/read-file.py`
- `session04/samples/text01.txt`
- `session04/samples/text02.txt`
- `session04/samples/text03.txt`
- `session04/samples/text04.txt`
- `session04/samples/text05.txt`
- `session04/samples/text06.txt`
- `session04/samples/text07.txt`
- `session04/samples/text_root.txt`
- `session04/samples/write-file.py`

### session05 — Dictionary/type samples

- `session05/samples/dict.py`

### session06 — Functions, recursion, and sorting samples

- `session06/samples/adder.py`
- `session06/samples/functions.py`
- `session06/samples/merge-sort.py`
- `session06/samples/recursive.py`

### session07 — Iterators, generators, decorators samples

- `session07/samples/decorators.py`
- `session07/samples/generators.py`
- `session07/samples/iterators.py`

### session09 — OOP basics samples

- `session09/samples/animal-class.py`
- `session09/samples/classes.py`
- `session09/samples/person.py`
- `session09/samples/wallet.py`
- `session09/samples/wallet_usage.py`

### session10 — OOP/inheritance samples

- `session10/samples/ball.py`
- `session10/samples/diamond.py`
- `session10/samples/encapsulation.py`
- `session10/samples/file-handler.py`
- `session10/samples/hovercraft.py`
- `session10/samples/lifecycle.py`
- `session10/samples/mixin.py`
- `session10/samples/shape.py`
- `session10/samples/todolist.py`

### session11 — Big-O, data structures, dataclass samples

- `session11/samples/bigo.py`
- `session11/samples/dataclass.py`
- `session11/samples/main.py`
- `session11/samples/my_queue.py`
- `session11/samples/stack.py`
- `session11/samples/two-sum.py`

### session15 — Advanced Python samples

- `session15/samples/context-manager.py`
- `session15/samples/iterators.py`
- `session15/samples/scopes.py`

### session17 — SQL samples

- `session17/samples/create_table.sql`
- `session17/samples/cross_join.sql`
- `session17/samples/simple_join.sql`

### session45 — Docker and Docker Compose samples

- `session45/samples/compose_postgres_logger/.dockerignore`
- `session45/samples/compose_postgres_logger/Dockerfile`
- `session45/samples/compose_postgres_logger/compose.yaml`
- `session45/samples/compose_postgres_logger/logger.py`
- `session45/samples/compose_postgres_logger/requirements.txt`
- `session45/samples/compose_redis_logger/.dockerignore`
- `session45/samples/compose_redis_logger/Dockerfile`
- `session45/samples/compose_redis_logger/compose.yaml`
- `session45/samples/compose_redis_logger/logger.py`
- `session45/samples/compose_redis_logger/requirements.txt`
- `session45/samples/config_reader/.dockerignore`
- `session45/samples/config_reader/Dockerfile`
- `session45/samples/config_reader/config.json`
- `session45/samples/config_reader/read_config.py`
- `session45/samples/greeting_app/.dockerignore`
- `session45/samples/greeting_app/Dockerfile`
- `session45/samples/greeting_app/greet.py`
- `session45/samples/looping_worker/.dockerignore`
- `session45/samples/looping_worker/Dockerfile`
- `session45/samples/looping_worker/worker.py`
- `session45/samples/report_writer/.dockerignore`
- `session45/samples/report_writer/Dockerfile`
- `session45/samples/report_writer/write_report.py`
- `session45/samples/simple_http/.dockerignore`
- `session45/samples/simple_http/Dockerfile`
- `session45/samples/simple_http/server.py`

## Structured Docker Samples

| Path | Used by | Purpose |
|------|---------|---------|
| `session45/samples/greeting_app/` | `S45P02-DockerfileImages.ipynb` | Simple `CMD` example and command override |
| `session45/samples/config_reader/` | `S45P02-DockerfileImages.ipynb` | Copying multiple files into a Docker image |
| `session45/samples/report_writer/` | `S45P02-DockerfileImages.ipynb` | Writing files and introducing bind mounts/volumes |
| `session45/samples/looping_worker/` | `S45P02-DockerfileImages.ipynb` | Detached containers, logs, stop/remove lifecycle |
| `session45/samples/simple_http/` | `S45P02-DockerfileImages.ipynb` | Request/response and port mapping |
| `session45/samples/compose_redis_logger/` | `S45P03-DockerCompose.ipynb` | Multi-container Compose project with Python + Redis |
| `session45/samples/compose_postgres_logger/` | `S45P03-DockerCompose.ipynb` | Optional Compose exercise with Python + PostgreSQL + volume |

## How to Run Samples

Many early samples are regular Python scripts:

```bash
python3 session02/samples/loop.py
```

Some SQL samples are intended to be opened or executed from a PostgreSQL client, depending on the lesson.

Dockerfile samples are run from their own directory:

```bash
cd session45/samples/greeting_app
docker build -t greeting_app .
docker run greeting_app
```

Compose samples are also run from their own directory:

```bash
cd session45/samples/compose_redis_logger
docker compose up --build
```

Check the related notebook for the expected commands, output, and cleanup steps.

## Maintenance Note

When adding a new `session*/samples/` file or mini-project, update this index so GitHub visitors can find runnable examples without browsing every session folder.
