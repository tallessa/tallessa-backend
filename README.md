# Tallessa – Effortless Asset Management

[![Build Status](https://travis-ci.org/tallessa/tallessa-backend.svg?branch=master)](https://travis-ci.org/tallessa/tallessa-backend)

## REST API

## Getting started

### The Docker Compose Way

There is a single unified Docker Compose development environment for both `tallessa-backend` (this repository) and [tallessa-frontend](https://github.com/tallessa/tallessa-backend).

First make sure you have both this repository and [tallessa-frontend](https://github.com/tallessa/tallessa-frontend) checked out under the same parent directory. Then, in the working copy of this repository, run

    docker-compose up

Backend will start at http://localhost:8000 and frontend dev server will start at http://localhost:8080. A default team called `hukassa` will be created along with a superuser `mahti` with password `mahti`.

### The Traditional Way

Requirements:

* Python 3.x (tested: Python 3.6)
* PostgreSQL 9.x (tested: PostgreSQL 9.5)

This assumes it's OK to create and access databases in PostgreSQL as your own user.

    python3 -m venv venv-tallessa
    source venv-tallessa/bin/activate
    pip install -U pip setuptools wheel

    git clone git@github.com:tallessa/tallessa-backend
    cd tallessa-backend
    pip install -r requirements.txt

    createdb -E UTF-8 tallessa
    DEBUG=true python manage.py setup

    DEBUG=true python manage.py runserver

## Coding conventions

Coding conventions are enforced via `isort` and `flake8`. We deviate from PEP-8 in the following points:

* Maximum line length is 120 Unicode characters
* Trailing commas are used in multi-line lists, dicts and function invocations

## License

    Tallessa – Effortless Asset Management (API backend)
    Copyright © 2016–2017 Santtu Pajukanta

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU Affero General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU Affero General Public License for more details.

    You should have received a copy of the GNU Affero General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
