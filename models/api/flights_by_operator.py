from ..models import Flights
from django.views import View
from django.shortcuts import render
from datetime import datetime
from django.http import JsonResponse,HttpResponse
from ..tools import categorize_flights


def get_flights_by_airoperator(request):
    air_operator = request.GET.get('operator')
    if not air_operator:
        return HttpResponse(status=404)
    future_flights = Flights.objects.filter(airoperator_name=air_operator,
                                            departure_1_date_time__gt=datetime.now()).order_by('departure_1_date_time')
    past_flights = Flights.objects.filter(airoperator_name=air_operator,
                                          departure_1_date_time__lte=datetime.now()).order_by('departure_1_date_time')
    data = {}
    data['future'] = categorize_flights(future_flights)
    data['past'] = categorize_flights(past_flights)

    return JsonResponse(data)
