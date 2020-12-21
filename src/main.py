import os
import sys

import jinja2 as jinja2
from fastapi import FastAPI, Request, HTTPException, Path
from fastapi.responses import PlainTextResponse
from jinja2 import UndefinedError, StrictUndefined, TemplateNotFound

try:
    templates_dir = os.environ['TEMPLAPI_DIR']
except KeyError:
    print(f'please set the environment variable TEMPLAPI_DIR to a directory path for templates', file=sys.stderr)
    sys.exit(1)

app = FastAPI(title='templapi', version='0.1.0', root_path=os.environ.get('TEMPLAPI_ROOT', ''))
jinja_env = jinja2.Environment(loader=jinja2.FileSystemLoader(searchpath=templates_dir), undefined=StrictUndefined)


@app.get('/j2/templates/{name}', response_class=PlainTextResponse,
         description='any query parameters will be used as jinja variables')
def get_jinja2(request: Request, name: str = Path(..., description='the name of the template')):
    try:
        return jinja_env.get_template(f'{name}.jinja').render(**request.query_params)
    except UndefinedError as error:
        raise HTTPException(status_code=400, detail=str(error))
    except TemplateNotFound:
        raise HTTPException(status_code=404, detail=f'template {name} not found')
