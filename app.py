from fastapi import FastAPI
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.requests import Request

templates = Jinja2Templates(directory='templates')
static = StaticFiles(directory='static')

app = FastAPI()
app.mount('/static', static, 'static')


@app.get('/')
async def index(request: Request):
    return templates.TemplateResponse('index.html', {'request': request})
