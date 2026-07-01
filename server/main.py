from fastapi import FastAPI
from server.routers import widgets, vm_stat

app = FastAPI(
    title="Homelab_API",
    version="1.0",
)

app.include_router(widgets.router, prefix='/api')
app.include_router(vm_stat.router, prefix='/api')

@app.get("/")
def get_home():
    return {"message": "Home"}
