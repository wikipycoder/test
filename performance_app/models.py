from django.db import models
from .managers import DailyPerformanceManager

class Performance(models.Model):

    cost = models.FloatField(default=0.0)
    revenue = models.FloatField(default=0.0)
    profit = models.FloatField(default=0.0)
    created_at = models.DateTimeField(auto_now_add=True)


class HourlyPerformance(Performance):
    datetime = models.DateTimeField()




class DailyPerformance(Performance):
    date = models.DateField()

    objects = DailyPerformanceManager()

