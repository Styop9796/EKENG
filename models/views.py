from django.shortcuts import render
from .models import Flights


# Create your views here.


def home_page(request):
    air_operators = Flights.objects.values_list('airoperator_name', flat=True).distinct()
    unique_names = list(air_operators)

    return render(request,'home_page.html',{'air_operators':unique_names})
