from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

app = FastAPI()

templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    data = {
        "page": "Home page"
    }
    return templates.TemplateResponse("home.html", {"request": request, "data": data})


@app.get("/base", response_class=HTMLResponse)
async def page(request: Request):
    data = {
        "page": page_name
    }
    return templates.TemplateResponse("base.html", {"request": request, "data": data})