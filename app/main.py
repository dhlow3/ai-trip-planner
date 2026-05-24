from fastapi import FastAPI

from app.routes.trips import router as trips_router


app = FastAPI()

app.include_router(trips_router)


@app.get("/")
def root() -> dict[str, str]:
    return {"message": "AI Trip Planner API"}


@app.get("/health")
def health_check() -> dict[str, str]:
    return {"status": "ok"}
