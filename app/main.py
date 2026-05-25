from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles

from app.models.trip_models import TripRequest, TripResponse
from app.routes.trips import generate_trip, router as trips_router


app = FastAPI()

app.mount("/static", StaticFiles(directory="app/static"), name="static")
app.include_router(trips_router)


@app.post("/generate-trip", response_model=TripResponse)
def generate_trip_from_frontend(trip_request: TripRequest) -> TripResponse:
    return generate_trip(trip_request)


@app.get("/")
def root() -> FileResponse:
    return FileResponse("app/static/index.html")


@app.get("/health")
def health_check() -> dict[str, str]:
    return {"status": "ok"}
