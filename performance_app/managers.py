from django.db import models


class DailyPerformanceManager(models.Manager):

    def filter_by_min_roi(self, min_roi: float):
        costs = sum(list(self.model.objects.values_list("cost", flat=True)))
        profit = sum(list(self.model.objects.values_list("profit", flat=True)))
        try:
            roi = (profit/costs)*100
        except ZeroDivisionError:
            roi = 0.0
    
        return roi

