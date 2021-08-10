# VAIT - GOVHACK Melbourne team - Backend Service

## Install

```bash
POETRY_VIRTUALENVS_IN_PROJECT=true poetry install
```

The `POETRY_VIRTUALENVS_IN_PROJECT=true` only needs to be run once to create the `backend/.venv` folder. Afterwards, just run `poetry install`.

## Local development

```bash
poetry shell
serverless wsgi serve
```

To exit the virtualenv created by poetry, type `exit` in the command line.

## Deployment

```bash
serverless deploy
```
