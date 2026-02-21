from fastapi import APIRouter
from typing import Optional

router = APIRouter(prefix="/alerts", tags=["alerts"])


@router.get("/")
async def list_alerts(
    active_only: bool = True,
    limit: int = 20,
):
    """List recent alerts."""
    return {
        "alerts": [],
        "total": 0,
    }


@router.get("/recent")
async def recent_alerts(hours: int = 24):
    """Get alerts from the last N hours."""
    return {
        "alerts": [],
        "period_hours": hours,
    }
