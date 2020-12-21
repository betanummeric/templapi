# templapi

This tiny HTTP api turns query parameters into template variables, renders a template and returns it.

Supported template languages:

- jinja

API docs are at: `GET /docs` and with different CSS at `GET /redoc`

### start it without docker:

```bash
pipenv sync
export TEMPLAPI_DIR="$PWD/templates"
pipenv run python src/launch.py
```

### start it with docker

```bash
docker build -t templapi .
docker run -it -p 3000:80 --mount type=bind,target=/srv/templates,source="$PWD/templates" templapi
```