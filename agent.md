# agent.md

Context file for AI agents working in this repository.

## Project Summary

A Jupyter notebook course repository for teaching Python programming (Maktab 141). The course currently contains 44 numbered sessions, progressing from Python fundamentals through Linux, databases, Django, Django REST Framework, Redis/Celery, and deployment.

## Environment

- **Runtime:** Python with JupyterLab 4.x / Notebook 7.x
- **Install deps:** `pip install -r requirement.txt`
- **Launch:** `jupyter lab` or `jupyter notebook`
- **Primary dependency file:** `requirement.txt`

`requirement.txt` is pinned and mainly describes the notebook/Jupyter environment. Later course topics such as Django, DRF, Redis, Celery, PostgreSQL, and deployment may be taught in notebooks without every runtime dependency being globally pinned here.

## Content Map

| Sessions | Topics |
|----------|--------|
| 01–04 | Python and computing basics: history, requirements, types, variables, operators, control flow, functions, PEPs, modules, encoding, file I/O, exceptions, numbering systems |
| 05–06 | Core data structures and functions: more types, dictionaries, strings, formatting, function details, sets |
| 07 | Iterators, generators, decorators |
| 08 | Git, GitHub, branching, advanced Git |
| 09–10 | Object-oriented programming (parts 1 & 2) |
| 11 | Big-O complexity, stack/queue, clean code, virtual environments |
| 12–13 | GNU/Linux intro, CLI commands, permissions/security, bash scripting |
| 14 | Networking, HTTP |
| 15 | Advanced Python |
| 16–18 | Databases: database concepts, PostgreSQL, SQL, joins, data manipulation, DDL, advanced DB topics, ERD design, psycopg2 |
| 19–31 | Django: intro, views and URLs, models, templates, forms, model fields, relationships, ORM tools, sessions/cookies, auth, custom users/signals, class-based views, management commands, logging |
| 32–41 | Django REST Framework: intro, class/generic views, viewsets/routers, serializers/testing, filtering/search/ordering, pagination, Swagger/OpenAPI docs, permissions, session auth, token auth, JWT |
| 42–43 | Redis, Django caching, Celery |
| 44 | Deployment with Nginx, Gunicorn, PostgreSQL, systemd, static/media handling |

## Current Notebook Inventory

| Session | Notebook(s) |
|---------|-------------|
| 01 | `S01P01-History.ipynb`, `S01P02-Requirements.ipynb`, `S01P03-Types, Variables, Operators.ipynb` |
| 02 | `S02-ControlStructures.ipynb` |
| 03 | `S03P01-Functions.ipynb`, `S03P02-PEP.ipynb`, `S03P03-Modules.ipynb` |
| 04 | `S04P01-CharacterEncoding.ipynb`, `S04P02-FileHandling.ipynb`, `S04P03-ExceptionHandling.ipynb`, `S04P04-NumberingSystem.ipynb` |
| 05 | `S05P01-MoreTypes.ipynb`, `S05P02-StringFormating.ipynb` |
| 06 | `S06P01-MoreAboutFunctions.ipynb`, `S06P02-Sets.ipynb` |
| 07 | `S07P01-Iteration.ipynb`, `S07P02-Decorators.ipynb` |
| 08 | `S08P01-VCS.ipynb`, `S08P02-GitIntro.ipynb`, `S08P03-GitHub.ipynb`, `S08P04-GitBranching.ipynb`, `S08P05-AdvancedGit.ipynb` |
| 09-15 | One notebook per session: OOP, OOP2, Big-O/venv/clean code, Linux, networking/HTTP, advanced Python |
| 16-18 | Database, PostgreSQL, SQL, joins, DML, DDL, advanced DB, ERD, psycopg2 |
| 19-31 | Django core notebooks |
| 32-41 | DRF notebooks |
| 42-44 | caching/Redis, Celery, deployment |

## File Conventions

- Notebooks: `S<session>[P<part>]-<Topic>.ipynb` (e.g. `S11P01-BigO.ipynb`, `S09-OOP.ipynb`)
- Each session folder may have `samples/` (runnable `.py` files) and `images/` (referenced in notebooks)
- Session folders use the format `sessionNN`, where `NN` is a two-digit sequential number.
- Some older filenames contain typos or historical naming choices, for example `StringFormating` and `AdvancePython`; preserve existing names unless explicitly asked to rename.
- `session16` currently has two `P02` notebooks: `S16P02-IntroPostgreSQL.ipynb` and `S16P02-IntroSQL.ipynb`. Treat this as existing course structure unless asked to renumber.

## Editing Guidelines

- All teaching content lives in `.ipynb` files — prefer editing notebooks over creating standalone scripts
- No test suite or linter is configured; `requirement.txt` is pinned and should not be changed without explicit instruction
- The `session*` folder numbering must stay sequential and consistent with the notebook naming convention above
- Keep notebooks valid JSON. Prefer structured notebook-aware tooling when making broad changes.
- Preserve educational tone and examples. This is a teaching repository, not an application codebase.
- Keep `samples/` files small and aligned with the notebook that references them.
- Do not remove or rename images without checking notebook references.
- Avoid changing generated notebook metadata unless the task requires it.

## Useful Commands

```bash
pip install -r requirement.txt
jupyter lab
jupyter notebook
```

Open a specific notebook:

```bash
jupyter lab session32/S32-DRFIntro.ipynb
```

Quick inventory checks:

```bash
find . -maxdepth 2 -type f -path './session*/*.ipynb' | sort
find . -maxdepth 3 -type f \( -path './session*/samples/*' -o -path './session*/images/*' \) | sort
```

## Git History Notes

- `4da14ab` added the original AI-agent context files.
- `78dee96` added sessions 22-38 as notebooks.
- `b484ef8` added more later-session material.
- `cdea0a2` reordered sessions 22-44 to match the syllabus sequence.

Because the agent docs predate the later session expansion, keep this file synchronized whenever sessions are added, removed, or renumbered.
