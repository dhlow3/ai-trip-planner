import json

from fastapi import APIRouter, HTTPException
from pydantic import ValidationError

from app.models.trip_models import TripRequest, TripResponse
from app.services.ai_service import generate_trip_recommendation


router = APIRouter(prefix="/trips", tags=["trips"])


@router.post("/generate-trip", response_model=TripResponse)
def generate_trip(trip_request: TripRequest) -> TripResponse:
    try:
        recommendation = generate_trip_recommendation(trip_request)
    except ValueError as error:
        raise HTTPException(status_code=500, detail=str(error))
    except Exception:
        raise HTTPException(status_code=502, detail="Could not generate a trip recommendation. Please try again.")

    try:
        data = json.loads(recommendation)
    except json.JSONDecodeError:
        raise HTTPException(status_code=500, detail="AI returned an unexpected response. Please try again.")

    try:
        return TripResponse(**data)
    except ValidationError:
        raise HTTPException(status_code=500, detail="AI response was missing required trip details. Please try again.")
