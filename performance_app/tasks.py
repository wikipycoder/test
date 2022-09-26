from .slow_iteration import fetch_daily_performance
from celery import shared_task

@shared_task(bind=True)
def fetching_data(self):
    fetch_daily_performance()
    return "Done"




