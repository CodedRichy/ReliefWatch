from datetime import datetime
from enum import Enum
from typing import Optional
from pydantic import BaseModel


class CrisisType(str, Enum):
    FOOD_INSECURITY = "food_insecurity"
    MEDICAL_EMERGENCY = "medical_emergency"
    DISPLACEMENT = "displacement"
    WATER_SANITATION = "water_sanitation"
    DISEASE_OUTBREAK = "disease_outbreak"
    CONFLICT = "conflict"
    OTHER = "other"


class Severity(str, Enum):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"
    CRITICAL = "critical"


class Source(BaseModel):
    platform: str
    url: str
    author: Optional[str] = None
    posted_at: datetime
    text: str


class Location(BaseModel):
    name: str
    admin_level: int
    latitude: Optional[float] = None
    longitude: Optional[float] = None
    country: str


class CrisisEvent(BaseModel):
    id: str
    crisis_type: CrisisType
    location: Location
    severity: Severity
    confidence: float
    signal_count: int
    sources: list[Source]
    first_detected: datetime
    last_updated: datetime
    summary: str
