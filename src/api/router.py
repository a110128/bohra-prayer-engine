from fastapi import APIRouter
from datetime import date
from ..calculation_engine import get_prayer_times

router = APIRouter()

@router.get("/prayer-times")
def prayer_times(lat: float, lon: float, day: str = None):
    if day is None:
        day = date.today().isoformat()
    return {
        "date": day,
        "location": {"lat": lat, "lon": lon},
        "times": get_prayer_times(lat, lon, day)
    }
