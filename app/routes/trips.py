import json

from fastapi import APIRouter, HTTPException
from pydantic import ValidationError

from app.models.trip_models import TripRequest, TripResponse
from app.services.ai_service import generate_trip_recommendation


router = APIRouter(prefix="/trips", tags=["trips"])


def trip_error(status_code: int, message: str) -> HTTPException:
    return HTTPException(status_code=status_code, detail=message)


def parse_trip_response(ai_response_text: str) -> TripResponse:
    try:
        trip_data = json.loads(ai_response_text)
    except json.JSONDecodeError:
        raise trip_error(500, "The AI returned text that was not valid JSON.")

    try:
        return TripResponse(**trip_data)
    except ValidationError:
        raise trip_error(500, "The AI response was missing required trip details.")


@router.post("/generate-trip", response_model=TripResponse)
def generate_trip(trip_request: TripRequest) -> TripResponse:
    try:
        ai_response_text = generate_trip_recommendation(trip_request)
    except ValueError:
        raise trip_error(500, "Could not generate a trip recommendation. Please try again.")
    except Exception:
        raise trip_error(502, "Could not generate a trip recommendation. Please try again.")

    return parse_trip_response(ai_response_text)
