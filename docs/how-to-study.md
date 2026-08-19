# How to Use This Repository

This repository can be used in class or for self-study.

## Recommended Workflow

1. Open notebooks in order when learning a topic for the first time.
2. Run code cells instead of only reading them.
3. Change small parts of examples and run again.
4. Use sample projects when a notebook references `samples/`.
5. Revisit previous sessions when later topics use earlier concepts.

## Running Notebooks

Install the notebook environment:

```bash
pip install -r requirement.txt
```

Start JupyterLab:

```bash
jupyter lab
```

Or classic notebook:

```bash
jupyter notebook
```

Open a specific notebook:

```bash
jupyter lab session45/S45P01-DockerBasics.ipynb
```

## Extra Tools by Topic

`requirement.txt` mainly describes the Jupyter/notebook runtime. Some later sessions require external tools.

| Topic | Extra tools you may need |
|-------|--------------------------|
| PostgreSQL / SQL | PostgreSQL server/client |
| Redis / caching / Celery | Redis |
| Deployment | Linux server/VPS, Nginx, Gunicorn, PostgreSQL |
| Docker | Docker Engine/Desktop and Docker Compose |

## Public Repository Notes

- This repository is teaching material, not an application with a normal test suite.
- Some notebooks are classroom notes and may intentionally stay compact.
- Some filenames are historical and preserved for compatibility.
- Real secrets such as `.env` files should not be committed.
