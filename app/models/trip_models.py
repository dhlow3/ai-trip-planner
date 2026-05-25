from typing import Literal

from pydantic import BaseModel, Field


class TripRequest(BaseModel):
    """What the user sends when requesting a trip plan."""

    destination: str = Field(..., min_length=2, examples=["Yosemite National Park"])
    activity: str = Field(..., min_length=2, examples=["hiking"])
    season: Literal["spring", "summer", "fall", "winter"] = Field(..., examples=["summer"])
    experience_level: Literal["beginner", "intermediate", "advanced"] = Field(..., examples=["beginner"])


class TripResponse(BaseModel):
    """What the AI returns after planning a trip."""

    destination: str
    activity: str
    season: Literal["spring", "summer", "fall", "winter"]
    experience_level: Literal["beginner", "intermediate", "advanced"]
    itinerary: list[str]
    packing_list: list[str]
    safety_tips: list[str]
