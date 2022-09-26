from .models import DailyPerformance
import random

def set_random_revenue():

    roi = DailyPerformance.objects.filter_by_min_roi(min_roi=0.5)
    daily_performances = DailyPerformance.objects.all()
    queryset_length = len(daily_performances)

    if roi > 50:
        print("length of the queryset: ", queryset_length)
        print("length of the queryset multiplied by 2: ", queryset_length*2)
        for index in range(queryset_length):
            print("{}/{}".format(index, queryset_length))
            daily_performance = daily_performances[index] 
            revenue = round(random.uniform(0.5, 2), 1)
            daily_performance.revenue = revenue
            daily_performance.save()