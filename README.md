# Python & Backend Development Notebooks

A public, reusable collection of Jupyter notebooks for teaching and learning Python and backend development. The material starts with Python fundamentals and grows into practical backend topics: Git/GitHub, Linux, databases/PostgreSQL, Django and Django REST Framework (DRF), Redis/Celery, Docker, and deployment.

This repository is organized as sequential sessions and is not tied to one specific course or cohort.

## Quick Links

- [Learning Roadmap](docs/roadmap.md)
- [Session Index](docs/sessions.md)
- [How to Use This Repository](docs/how-to-study.md)
- [Sample Projects Index](docs/samples.md)

## Topics Covered

| Sessions | Topics |
|----------|--------|
| 01–07 | Python foundations: basics, functions, files, exceptions, data structures, iteration, decorators |
| 08, 11–14 | Git/GitHub, virtual environments, clean code, Linux, networking, HTTP |
| 09–10 | Object-oriented programming |
| 15 | Advanced Python |
| 16–18 | Databases: PostgreSQL, SQL, joins, DML/DDL, design, psycopg |
| 19–31 | Django core: views, URLs, models, templates, forms, ORM, auth, CBVs, management commands, logging |
| 32–41 | Django REST Framework: APIs, serializers, viewsets, testing, Swagger/OpenAPI, permissions, auth, JWT |
| 42–43 | Redis, Django caching, Celery |
| 44 | Deployment with Nginx, Gunicorn, PostgreSQL, systemd, static/media handling |
| 45–46 | Docker fundamentals, Docker Compose, Dockerized Django deployment |

## Repository Structure

- `sessions/sessionNN/` — numbered session folders.
- `*.ipynb` — teaching notebooks. Names usually follow `S<session>[P<part>]-<Topic>.ipynb`.
- `sessions/sessionNN/samples/` — small runnable examples used by notebooks.
- `sessions/sessionNN/images/` — image assets referenced by notebooks.
- `docs/` — roadmap, session index, study guide, and sample index.
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
jupyter lab sessions/session45/S45P01-DockerBasics.ipynb
```

## Notes

- `requirement.txt` mainly describes the notebook/Jupyter runtime. Later topics such as Django, DRF, Redis, Celery, PostgreSQL, Docker, and deployment may need extra tools.
- Some historical filenames are intentionally preserved even if they contain typos or older naming choices.
- This repository is teaching material, not an application codebase with a configured test suite.
- Licensed under the repository's [Creative Commons Attribution-ShareAlike 4.0 International license](LICENSE).
