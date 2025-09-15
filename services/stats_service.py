from sqlalchemy.orm import Session

# internal package
import models

def calculate_stats(db:Session):
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

