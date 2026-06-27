from fastapi import APIRouter, Depends, HTTPException, status

router = APIRouter(prefix="/dashboard", tags=["dashboard"])

@router.get("/{programm_id}")
def get_programm_status(programm_id: int):
    
    return {"status": "started"}