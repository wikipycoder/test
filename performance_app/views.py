from django.shortcuts import render
from django.http import HttpResponse
from .tasks import fetching_data


def fetch(request):

    fetching_data.delay()
    return HttpResponse("data fetched")    

    