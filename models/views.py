from django.shortcuts import render
from .models import Flights
from django.http import HttpResponse


# Create your views here.


def home_page(request):  # Render home page with all airoperators info
    air_operators = Flights.objects.values_list('airoperator_name', flat=True).distinct()
    unique_names = list(air_operators)

    return render(request, 'home_page.html', {'air_operators': unique_names})


def air_operator_page(request, operator):  # Render air operator page
    air_operator_flights = Flights.objects.filter(airoperator_name=operator)
    if air_operator_flights:
        return render(request, 'operator_page.html', {'operator': operator})
    else:
        return HttpResponse(status=404)


def top_flights(request):  # Render top flights page
    return render(request, 'top_flights.html')
