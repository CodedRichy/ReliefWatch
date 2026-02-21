from fastapi import APIRouter, Query
from typing import Optional
from ..models.event import CrisisType, Severity

router = APIRouter(prefix="/events", tags=["events"])


@router.get("/")
async def list_events(
    crisis_type: Optional[CrisisType] = None,
    severity: Optional[Severity] = None,
    country: Optional[str] = None,
    limit: int = Query(default=50, le=100),
    offset: int = 0,
):
    """List crisis events with optional filters."""
    return {
        "events": [],
        "total": 0,
        "limit": limit,
        "offset": offset,
    }


@router.get("/{event_id}")
async def get_event(event_id: str):
    """Get a specific crisis event by ID."""
    return {"error": "not_found", "message": f"Event {event_id} not found"}


@router.get("/stats/summary")
async def get_stats():
    """Get summary statistics for current crisis events."""
    return {
        "total_events": 0,
        "by_type": {},
        "by_severity": {},
        "by_country": {},
    }
