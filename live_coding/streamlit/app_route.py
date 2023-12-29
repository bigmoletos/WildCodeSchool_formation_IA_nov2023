from fastapi import FastAPI
from fastapi.middleware.wsgi import WSGIMiddleware
import streamlit as st
from starlette.applications import Starlette
from starlette.routing import Route, Mount
from starlette.staticfiles import StaticFiles
from starlette.responses import JSONResponse
from starlette.templating import Jinja2Templates

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/iris")
def read_iris():
    return {"Page": "Iris"}

@app.get("/titanic")
def read_titanic():
    return {"Page": "Titanic"}

@app.post("/iris")
def create_iris():
    return {"Page": "Iris"}

@app.post("/titanic")
def create_titanic():
    return {"Page": "Titanic"}

st_app = WSGIMiddleware(st)
app.mount("/", st_app)
