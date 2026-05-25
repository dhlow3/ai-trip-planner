from openai import OpenAI

from app.config import settings
from app.models.trip_models import TripRequest


MODEL_NAME = "gpt-4.1-mini"
SYSTEM_PROMPT = (
    "You are an expert outdoor travel guide. "
    "Always respond with valid JSON only — no markdown, no commentary. "
    "Be concise: 3–5 items per list, one sentence per itinerary day."
)
RESPONSE_FORMAT = """{
  "destination": "string",
  "activity": "string",
  "season": "string",
  "experience_level": "string",
  "itinerary": ["Day 1: ...", "Day 2: ...", ...],
  "packing_list": ["item 1", "item 2", ...],
  "safety_tips": ["tip 1", "tip 2", ...]
}"""

client = OpenAI(api_key=settings.openai_api_key)


def build_user_prompt(trip_request: TripRequest) -> str:
    return f"""Plan a {trip_request.experience_level}-level {trip_request.activity} trip.

Destination: {trip_request.destination}
Season: {trip_request.season}

Return JSON with exactly these keys:
{RESPONSE_FORMAT}"""


def generate_trip_recommendation(trip_request: TripRequest) -> str:
    user_prompt = build_user_prompt(trip_request)

    response = client.responses.create(
        model=MODEL_NAME,
        instructions=SYSTEM_PROMPT,
        input=user_prompt,
        text={"format": {"type": "json_object"}},
    )

    if not response.output_text:
        raise ValueError("AI returned an empty response.")

    return response.output_text
