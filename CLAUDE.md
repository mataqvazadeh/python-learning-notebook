# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## About

A collection of Jupyter notebooks for a Python programming course (Maktab 141). The repository currently has 44 sequential session folders, from Python basics through Django, Django REST Framework, Redis/Celery, and deployment. Each session folder contains one or more `.ipynb` notebooks and may include `samples/` and `images/` subdirectories.

For fuller cross-agent guidance, also read `agent.md`.

## Setup

```bash
pip install -r requirement.txt
```

## Running Notebooks

```bash
jupyter lab        # full JupyterLab UI
jupyter notebook   # classic notebook UI
```

Open a specific notebook directly:

```bash
jupyter lab session09/S09-OOP.ipynb
```

## Repository Structure

Sessions are numbered sequentially and cover:

| Sessions | Topics |
|----------|--------|
| 01–04 | Python basics: history, requirements, types, operators, control structures, functions, PEPs, modules, encoding, file/exception handling |
| 05–06 | Core data structures and function topics: more types, dictionaries, string formatting, sets |
| 07 | Iterators, generators, decorators |
| 08 | Version control: Git, GitHub, branching |
| 09–10 | Object-oriented programming (OOP parts 1 & 2) |
| 11 | Big-O complexity, data structures (stack, queue), clean code, virtual environments |
| 12–13 | Linux intro, commands, security, bash scripting |
| 14 | Networking and HTTP |
| 15 | Advanced Python |
| 16–18 | Databases: SQL, PostgreSQL, DDL, advanced DB, design, psycopg2 |
| 19–31 | Django: intro, views & URLs, models, templates, forms, ORM, sessions/cookies, auth, custom users/signals, CBVs, management commands, logging |
| 32–41 | Django REST Framework: intro, generic views, viewsets/routers, serializers/testing, filtering/search/ordering, pagination, Swagger/OpenAPI, permissions, token auth, JWT |
| 42–43 | Redis, Django caching, Celery |
| 44 | Deployment: Nginx, Gunicorn, PostgreSQL, systemd |

## Notebook Naming Convention

`S<session><part>-<Topic>.ipynb` — e.g., `S11P01-BigO.ipynb` is session 11, part 1.
Single-part sessions drop the part number: `S09-OOP.ipynb`.

Session folders use `sessionNN`, for example `session01` and `session44`.

## Editing Notes

- Prefer editing existing notebooks for teaching content instead of adding standalone scripts.
- Keep `requirement.txt` pinned unless explicitly asked to update dependencies.
- Preserve existing filenames unless a rename is specifically requested. Some historical names contain typos or duplicate part numbers, such as `S05P02-StringFormating.ipynb` and the two `session16/S16P02-*` notebooks.
- Keep notebook JSON valid and avoid unrelated metadata churn.
- Do not rename or delete files in `images/` or `samples/` without checking notebook references.
- There is no configured test suite or linter for the repository.

## Git Context

The original agent files were added in commit `4da14ab`. Later commits added and reordered sessions 22-44, especially `78dee96`, `b484ef8`, and `cdea0a2`, so older documentation that mentions only sessions 01-21 is stale.
