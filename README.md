# Python & Backend Development Notebooks

A public, reusable collection of Jupyter notebooks for teaching and learning Python and backend development. The material starts with Python fundamentals and grows into practical backend topics: Git and GitHub, Linux, databases and PostgreSQL, Django and Django REST Framework (DRF) as Python backend frameworks, Redis/Celery, Docker, and deployment. It is organized as sequential sessions and is not tied to one specific course or cohort.

## Topics Covered

| Sessions | Topics |
|----------|--------|
| 01–04 | Python and computing basics: history, requirements, types, variables, operators, control flow, functions, PEPs, modules, encoding, file I/O, exceptions, numbering systems |
| 05–06 | Core data structures and functions: more types, dictionaries, strings, formatting, function details, sets |
| 07 | Iterators, generators, decorators |
| 08 | Git, GitHub, branching, advanced Git |
| 09–10 | Object-oriented programming |
| 11 | Big-O complexity, stack/queue, clean code, virtual environments |
| 12–13 | GNU/Linux intro, CLI commands, permissions/security, bash scripting |
| 14 | Networking and HTTP |
| 15 | Advanced Python |
| 16–18 | Databases: PostgreSQL, SQL, joins, DML, DDL, advanced DB topics, ERD design, psycopg2 |
| 19–31 | Django: intro, views and URLs, models, templates, forms, ORM, sessions/cookies, auth, custom users/signals, class-based views, management commands, logging |
| 32–41 | Django REST Framework: intro, class/generic views, viewsets/routers, serializers/testing, filtering/search/ordering, pagination, Swagger/OpenAPI docs, permissions, token auth, JWT |
| 42–43 | Redis, Django caching, Celery |
| 44 | Deployment with Nginx, Gunicorn, PostgreSQL, systemd, static/media handling |
| 45 | Docker fundamentals: containers, images, volumes, Dockerfile, custom images, Docker Compose |

## Repository Structure

- `sessionNN/` — numbered session folders.
- `*.ipynb` — teaching notebooks. Notebook names usually follow `S<session>[P<part>]-<Topic>.ipynb`.
- `samples/` — small runnable examples used by notebooks.
- `images/` — image assets referenced by notebooks.
- `requirement.txt` — pinned dependencies for the Jupyter/notebook environment.

## Setup

Install dependencies:

```bash
pip install -r requirement.txt
```

Run JupyterLab:

```bash
jupyter lab
```

Or run the classic notebook interface:

```bash
jupyter notebook
```

Open a specific notebook directly:

```bash
jupyter lab session09/S09-OOP.ipynb
```

## Notes

- `requirement.txt` mainly describes the notebook/Jupyter runtime. Later topics such as Django, DRF, Redis, Celery, PostgreSQL, and deployment may be taught without every runtime dependency being globally pinned here.
- Some historical filenames are intentionally preserved even if they contain typos or older naming choices.
- This repository is teaching material, not an application codebase with a configured test suite.
