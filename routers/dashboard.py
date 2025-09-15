from fastapi import APIRouter ,status, HTTPException , Depends
from typing import Annotated , List
from sqlalchemy.orm import Session


from database import get_db
import models
from services.stats import calculate_stats

router = APIRouter(prefix='/dashboard', tags=['dashboard'])

@router.get('/recaptcha/stats')
def dashboard_stats(db:Annotated[Session,Depends(get_db)]):
    return calculate_stats(db)