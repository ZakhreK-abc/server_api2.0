from fastapi import APIRouter, Depends, HTTPException, status
import requests
from server.service.weather import weather

router = APIRouter(prefix="/dashboard/widgets", tags=["widgets"])

@router.get("/weather")
def get_weather():
    data = weather()
    return data

