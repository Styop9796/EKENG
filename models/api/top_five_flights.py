from ..models import Flights
from django.http import JsonResponse


def get_top_five(request):
    x = Flights.objects.first()
    top = x.top_five_flights()
    sorted_items = sorted(top.items(), key=lambda x: x[1], reverse=True)
    items = [*sorted_items[:5]]
    formatted_data = {}
    for i in items:
        formatted_data[i[0][1]] = [i[1], i[0][0]]
    return JsonResponse(formatted_data)
