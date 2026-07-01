from fastapi import FastAPI
from server.routers import widgets

app = FastAPI(
    title="Homelab_API",
    version="1.0",
)

app.include_router(widgets.router, prefix='/api')


@app.get("/")
def get_home():
    return {"message": "Home"}
