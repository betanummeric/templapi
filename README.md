# templapi

This tiny HTTP api turns query parameters into template variables, renders a template and returns it.

Supported template languages:

- [jinja](https://jinja.palletsprojects.com/)

API docs are at: `GET /docs` and with different CSS at `GET /redoc`

### start it without docker:

1. install [pipenv](https://pipenv.pypa.io/)

```bash
pipenv sync
export TEMPLAPI_DIR="$PWD/templates"
pipenv run python src/launch.py
```

### start it with docker

1. install [docker](https://docs.docker.com/get-docker/)

```bash
docker build -t templapi .
docker run -it -p 3000:80 --mount type=bind,target=/srv/templates,source="$PWD/templates" templapi
```
