from app import App, templates
from fastapi import Request

@App.get("/")
async def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

