import datetime

from django.shortcuts import render
import pandas as pd
from ..models import Flights
from ..tools import parse_datetime


# Create your views here.
def load_data_from_excel(request):
    if request.method == 'POST':
        excel_file = request.FILES['excelFile']
        try:
            df = pd.read_excel(excel_file)
            for index, row in df.iterrows():
                uuid = row['uuid']
                created = row['created']
                task_id = row['task_id']
                arrival_1 = row['arrival_1']
                flight_no = row['flight_no']
                sign_date = parse_datetime(row['sign_date'])
                departure_1 = row['departure_1']
                traffic_type = row['traffic_type']
                permission_no = row['permission_no']
                airoperator_name = row['airoperator_name']
                place_of_business = row['place_of_business']
                arrival_1_date_time = parse_datetime(row['arrival_1_date_time'])
                departure_1_date_time = parse_datetime(row['departure_1_date_time'])
                print(arrival_1_date_time,"=",departure_1_date_time)
                new_value = Flights.objects.create(uuid=uuid,
                                                   created=str(created),
                                                   task_id=task_id,
                                                   arrival_1=arrival_1,
                                                   flight_no=flight_no,
                                                   sign_date=str(sign_date),
                                                   departure_1=departure_1,
                                                   traffic_type=traffic_type,
                                                   permission_no=permission_no,
                                                   airoperator_name=airoperator_name,
                                                   place_of_business=place_of_business,
                                                   arrival_1_date_time=str(arrival_1_date_time),
                                                   departure_1_date_time=str(departure_1_date_time))
                new_value.save()

            return render(request, 'upload_template.html', {'message': 'File uploaded and processed successfully.'})

        except Exception as e:
            return render(request, 'upload_template.html', {'error': str(e)})
    return render(request, 'upload_template.html')
