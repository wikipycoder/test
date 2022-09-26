from django.test import TestCase
from performance_app.models import Performance, DailyPerformance, HourlyPerformance
from datetime import date, datetime



class PerformanceTest(TestCase):

    def test_performane(self):

        values = {"profit": 34, "revenue": 12, "cost": 234}   
        performance = Performance.objects.create(**values)
        self.assertNotEquals(performance, None)
        performance.delete()
    

class DailyPerformanceTest(TestCase):

    def setUp(self):
        pass

    def test_daily_performance(self):

        date_objects = [date.today(), date.today()]
        daily_performances = [DailyPerformance.objects.create(date=date) for date in date_objects]

        for index, element in enumerate(date_objects):
            self.assertEquals(daily_performances[index].date, element)
        
        for daily_performance in daily_performances:
            daily_performance.delete()
        

class HourlyPerformanceTest(TestCase):

    def setUp(self):
        pass

    def test_hourly_performance(self):

        datetime_objects = [datetime.now(), datetime.now()]
        hourly_performances = [HourlyPerformance.objects.create(datetime=datetime) for datetime in datetime_objects]

        for index, element in enumerate(datetime_objects):
            self.assertEquals(hourly_performances[index].datetime, element)
        
        for hourly_performance in hourly_performances:
            hourly_performance.delete()








        


















    







            


