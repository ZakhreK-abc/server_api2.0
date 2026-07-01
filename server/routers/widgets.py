from fastapi import APIRouter, Depends, HTTPException, status
import requests
from server.service.weather import weather
from server.service.runline import run_line

router = APIRouter(prefix="/dashboard/widgets", tags=["widgets"])

@router.get("/weather")
def get_weather():
    data = weather()
    return data

@router.get("run-line/{type}")
def get_line(type:int):
    data = run_line(type)
    return data
