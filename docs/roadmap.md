# Learning Roadmap

This repository is organized as a progressive backend-development learning path.

```text
Python fundamentals
  ↓
Functions, files, exceptions, modules
  ↓
Data structures, iteration, decorators
  ↓
Git/GitHub, Linux, networking, HTTP
  ↓
PostgreSQL, SQL, database design
  ↓
Django core
  ↓
Django REST Framework
  ↓
Redis, caching, Celery
  ↓
Deployment with Nginx, Gunicorn, PostgreSQL
  ↓
Docker, Docker Compose, Dockerized Django deployment
```

## Main Stages

| Stage | Sessions | Focus |
|-------|----------|-------|
| Python foundations | 01–07 | Programming basics, functions, files, exceptions, data structures, iteration, decorators |
| Development tools | 08, 11–14 | Git/GitHub, virtual environments, clean code, Linux, networking, HTTP |
| Databases | 16–18 | PostgreSQL, SQL, joins, DML/DDL, design, psycopg |
| Django | 19–31 | Views, URLs, models, templates, forms, ORM, auth, CBVs, management commands, logging |
| Django REST Framework | 32–41 | APIs, serializers, viewsets, testing, Swagger/OpenAPI, permissions, auth, JWT |
| Async/cache/deployment | 42–44 | Redis, caching, Celery, Nginx, Gunicorn, PostgreSQL deployment |
| Docker | 45–46 | Docker fundamentals, Docker Compose, Dockerized Django deployment |

## Suggested Study Flow

1. Study notebooks in order when you are new to the topic.
2. Run code cells locally instead of only reading them.
3. Modify examples and observe the result.
4. Use `samples/` projects when a notebook references them.
5. For later backend topics, expect extra tools such as PostgreSQL, Redis, Docker, or a VPS.

## Notes

- The repository is reusable teaching material, not tied to one specific course or cohort.
- Later topics may require tools that are not installed by `requirement.txt`.
- Some historical filenames are preserved for compatibility.
