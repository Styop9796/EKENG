from ..models import Flights
from django.views import View
from django.shortcuts import render
from datetime import datetime
from django.http import JsonResponse

def get_flights_by_airoperator(request):
    print(datetime.now())
    air_operator = request.GET.get('operator')
    print(air_operator)
    future_flights = Flights.objects.filter(airoperator_name=air_operator,departure_1_date_time__gt=datetime.now()).order_by('departure_1_date_time')
    past_flights = Flights.objects.filter(airoperator_name=air_operator,departure_1_date_time__lte=datetime.now()).order_by('departure_1_date_time')
    serializable_data = {}
    serializable_data['future'] = [item.to_dict() for item in future_flights]
    serializable_data['past'] = [item.to_dict() for item in past_flights]
    return JsonResponse(serializable_data)