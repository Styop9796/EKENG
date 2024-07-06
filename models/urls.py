from django.urls import path
from .api.load_data_in_db import load_data_from_excel
from .api.flights_by_operator import get_flights_by_airoperator
from .api.permission_number import get_permission_numbers
from .api.top_five_flights import get_top_five
from .views import home_page, air_operator_page, top_flights

urlpatterns = [
    path('', home_page, name='home_page'),
    path('load/', load_data_from_excel, name='insert_data_into_db'),
    path('get/flights/', get_flights_by_airoperator, name='get_flights'),
    path('permission/numbers/', get_permission_numbers, name='get_permission_numbers'),
    path('<str:operator>/', air_operator_page, name='page_for_airoperator'),
    path('top/flights/', top_flights, name='top_5_flights'),
    path('top/flights/api/', get_top_five, name='api_for_top_5')

]
