import time
from .models import DailyPerformance


def fetch_daily_performance():
    
    daily_performances = DailyPerformance.objects.all()[:50]
    for daily_performance in daily_performances:
        time.sleep(60)
        





