from django.urls import path
from .api.load_data_in_db import load_data_from_excel
from .api.flights_by_operator import get_flights_by_airoperator
from .views import home_page
urlpatterns = [
    path('',home_page),
    path('load/',load_data_from_excel),
    path('get/flights/',get_flights_by_airoperator)
]