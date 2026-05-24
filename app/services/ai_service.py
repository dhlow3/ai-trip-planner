from openai import OpenAI

from app.config import settings
from app.models.trip_models import TripRequest


MODEL_NAME = "gpt-4.1-mini"

client = OpenAI(api_key=settings.openai_api_key)


def generate_trip_recommendation(trip_request: TripRequest) -> str:

    system_prompt = (
        "You are an expert outdoor travel guide. "
        "Always respond with valid JSON only — no markdown, no commentary. "
        "Be concise: 3–5 items per list, one sentence per itinerary day."
    )

    user_prompt = f"""Plan a {trip_request.experience_level}-level {trip_request.activity} trip.

Destination: {trip_request.destination}
Season: {trip_request.season}

Return JSON with exactly these keys:
{{
  "destination": "string",
  "activity": "string",
  "season": "string",
  "experience_level": "string",
  "itinerary": ["Day 1: ...", "Day 2: ...", ...],
  "packing_list": ["item 1", "item 2", ...],
  "safety_tips": ["tip 1", "tip 2", ...]
}}"""

    response = client.responses.create(
        model=MODEL_NAME,
        instructions=system_prompt,
        input=user_prompt,
        text={"format": {"type": "json_object"}},
    )

    return response.output_text
