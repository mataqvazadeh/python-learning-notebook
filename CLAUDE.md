# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## About

A collection of Jupyter notebooks for a Python programming course (Maktab 141). Each session folder contains one or more `.ipynb` notebooks and optional `samples/` and `images/` subdirectories.

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
| 01–04 | Python basics: types, control structures, functions, file/exception handling |
| 05–06 | Data structures: more types, string formatting, sets |
| 07 | Iterators, generators, decorators |
| 08 | Version control: Git, GitHub, branching |
| 09–10 | Object-oriented programming (OOP parts 1 & 2) |
| 11 | Big-O complexity, data structures (stack, queue), clean code, virtual environments |
| 12–13 | Linux intro, commands, security, bash scripting |
| 14 | Networking and HTTP |
| 15 | Advanced Python |
| 16–18 | Databases: SQL, PostgreSQL, DDL, advanced DB, design, psycopg2 |
| 19–21 | Django: intro, views & URLs, models |

## Notebook Naming Convention

`S<session><part>-<Topic>.ipynb` — e.g., `S11P01-BigO.ipynb` is session 11, part 1.
Single-part sessions drop the part number: `S09-OOP.ipynb`.
