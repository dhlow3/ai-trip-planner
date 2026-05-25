from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles

from app.routes.trips import router as trips_router


app = FastAPI()

app.mount("/static", StaticFiles(directory="app/static"), name="static")
app.include_router(trips_router)


@app.get("/")
def root() -> FileResponse:
    return FileResponse("app/static/index.html")


@app.get("/health")
def health_check() -> dict[str, str]:
    return {"status": "ok"}
