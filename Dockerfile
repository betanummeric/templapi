FROM python:3.9-alpine
RUN pip install --no-cache-dir --quiet pipenv && mkdir -p /srv/templates
WORKDIR /srv
COPY Pipfile Pipfile.lock /srv/
RUN pipenv sync --bare --keep-outdated --clear
VOLUME /srv/templates
ENV TEMPLAPI_DIR=/srv/templates
EXPOSE 80
COPY src /srv/
CMD ["/usr/local/bin/pipenv", "run", "uvicorn", "--port", "80", "--host", "0.0.0.0", "main:app"]
