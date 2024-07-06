from ..models import Flights
from datetime import datetime, time
from django.http import JsonResponse, HttpResponse
from ..tools import categorize_flights


def get_flights_by_airoperator(request):
    air_operator = request.GET.get('operator')
    start_time = request.GET.get('start_time')
    end_time = request.GET.get('end_time')

    current_datetime = datetime.now()
    if not air_operator:
        return HttpResponse(status=404)

    if start_time:
        start_time_obj = time(hour=int(start_time.split(':')[0]), minute=int(start_time.split(':')[1]))
    else:
        start_time_obj = None

    if end_time:
        end_time_obj = time(hour=int(end_time.split(':')[0]), minute=int(end_time.split(':')[1]))
    else:
        end_time_obj = None

    if start_time_obj and end_time_obj:
        future_flights = Flights.objects.filter(airoperator_name=air_operator,
                                                departure_1_date_time__time__gte=start_time_obj,
                                                departure_1_date_time__time__lte=end_time_obj,
                                                departure_1_date_time__gt=current_datetime).order_by(
            'departure_1_date_time')

        past_flights = Flights.objects.filter(airoperator_name=air_operator,
                                              departure_1_date_time__time__gte=start_time_obj,
                                              departure_1_date_time__time__lte=end_time_obj,
                                              departure_1_date_time__lte=current_datetime).order_by(
            'departure_1_date_time')


    else:
        future_flights = Flights.objects.filter(airoperator_name=air_operator,
                                                departure_1_date_time__gt=current_datetime).order_by(
            'departure_1_date_time')

        past_flights = Flights.objects.filter(airoperator_name=air_operator,
                                              departure_1_date_time__lte=current_datetime).order_by(
            'departure_1_date_time')
    data = {}
    data['future'] = categorize_flights(future_flights)
    data['past'] = categorize_flights(past_flights)
    return JsonResponse(data)
