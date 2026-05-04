# agent.md

Context file for AI agents working in this repository.

## Project Summary

A Jupyter notebook course repository for teaching Python programming (Maktab 141). Contains 21 sessions of educational content progressing from Python basics to Django web development.

## Environment

- **Runtime:** Python with JupyterLab 4.x / Notebook 7.x
- **Install deps:** `pip install -r requirement.txt`
- **Launch:** `jupyter lab` or `jupyter notebook`

## Content Map

| Sessions | Topics |
|----------|--------|
| 01–04 | Python basics: types, variables, operators, control flow, functions, file I/O, exception handling, encoding |
| 05–06 | Data structures: dicts, strings, sets, formatting |
| 07 | Iterators, generators, decorators |
| 08 | Git, GitHub, branching, advanced Git |
| 09–10 | Object-oriented programming (parts 1 & 2) |
| 11 | Big-O complexity, stack/queue, clean code, virtual environments |
| 12–13 | Linux CLI, security, bash scripting |
| 14 | Networking, HTTP |
| 15 | Advanced Python |
| 16–18 | SQL, PostgreSQL, DDL, database design, psycopg2 |
| 19–21 | Django: intro, views & URLs, models |

## File Conventions

- Notebooks: `S<session>[P<part>]-<Topic>.ipynb` (e.g. `S11P01-BigO.ipynb`, `S09-OOP.ipynb`)
- Each session folder may have `samples/` (runnable `.py` files) and `images/` (referenced in notebooks)

## Constraints

- All teaching content lives in `.ipynb` files — prefer editing notebooks over creating standalone scripts
- No test suite or linter is configured; `requirement.txt` is pinned and should not be changed without explicit instruction
- The `session*` folder numbering must stay sequential and consistent with the notebook naming convention above
