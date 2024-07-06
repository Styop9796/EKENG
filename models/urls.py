from django.urls import path
from .api.load_data_in_db import load_data_from_excel
from .api.flights_by_operator import get_flights_by_airoperator
from .api.permission_number import get_permission_numbers
from .views import home_page,air_operator_page,top_flights
urlpatterns = [
    path('',home_page),
    path('load/',load_data_from_excel),
    path('get/flights/',get_flights_by_airoperator),
    path('permission/numbers/',get_permission_numbers),
    path('<str:operator>/',air_operator_page),
    path('top/flights/',top_flights)

]