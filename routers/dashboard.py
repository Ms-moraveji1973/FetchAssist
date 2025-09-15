from fastapi import APIRouter ,status, HTTPException , Depends
from typing import Annotated , List
from sqlalchemy.orm import Session
from .solvers import get_db
import models
from schema import DashboardResponse ,LogSchema

router = APIRouter(prefix='/dashboard', tags=['dashboard'])

@router.get('/stats')
def dashboard_stats(db:Annotated[Session,Depends(get_db)]):
    logs = db.query(models.Logs).all()
    total = len(logs)
    success = sum(1 for i in logs if i.error_message is None)
    duration_average = round(sum(i.duration for i in logs) / total, 2) if total > 0 else 0

    stats = {
        'total': total,
        'success': success,
        'win_rate' : round(success / total * 100, 2),
        'duration_average': round(duration_average,2),
    }

    return {
        'logs': logs,
        'stats':  stats
    }

