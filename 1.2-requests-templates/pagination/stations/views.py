from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.paginator import Paginator
from django.conf import settings

import csv


def index(request):
    print(reverse('bus_stations'))
    return redirect(reverse('bus_stations'))

with open(settings.BUS_STATION_CSV, encoding='utf-8') as file:
    print(settings.BUS_STATION_CSV)
    data = [i for i in csv.DictReader(file)]
    for i in data[:10]:
        print(i)
    print(type(data))
    print(len(data))
def bus_stations(request):
    paginator = Paginator(data, 10)
    page_number = request.GET.get("page", 1)
    page = paginator.get_page(page_number)
    context = {
        'bus_stations': page,
        'page': page,
    }
    return render(request, 'stations/index.html', context)
