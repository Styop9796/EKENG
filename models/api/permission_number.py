from datetime import datetime, time
from django.shortcuts import render
from ..models import Flights
from ..tools import filter_permission_numbers
from django.http import JsonResponse


def get_permission_numbers(request):
    start_date = request.GET.get('start_date')
    end_date = request.GET.get('end_date')
    dt_start_date_with_time = None
    dt_end_date_with_time = None
    try:
        dt_start_date = datetime.strptime(start_date, '%Y-%m-%d').date()
        dt_end_date = datetime.strptime(end_date, '%Y-%m-%d').date()
        dt_start_date_with_time = datetime.combine(dt_start_date, time.min)
        dt_end_date_with_time = datetime.combine(dt_end_date, time.max)
    except Exception as e:
        pass
    if dt_start_date_with_time and dt_end_date_with_time:
        permission_numbers = Flights.objects.filter(sign_date__gte=dt_start_date_with_time,
                                                    sign_date__lte=dt_end_date_with_time)
        permission_number_dict = filter_permission_numbers(permission_numbers)
        return JsonResponse(permission_number_dict)
    return render(request, 'permissions_page.html')
