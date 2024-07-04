from django.db import models


class Flights(models.Model):

    uuid = models.CharField(max_length=100, primary_key=True)
    created = models.DateTimeField()
    task_id = models.IntegerField()
    arrival_1 = models.CharField(max_length=10,blank=True)
    flight_no = models.CharField(max_length=20)
    sign_date = models.DateTimeField()
    departure_1 = models.CharField(max_length=10,blank=True)
    traffic_type = models.CharField(max_length=20,blank=True)
    permission_no = models.CharField(max_length=20)
    airoperator_name = models.CharField(max_length=100)
    place_of_business = models.CharField(max_length=50)
    arrival_1_date_time = models.DateTimeField()
    departure_1_date_time = models.DateTimeField()


    def to_dict(self):
        return {
            'uuid': self.uuid,
            'created': self.created,
            'task_id': self.task_id,
            'arrival_1': self.arrival_1,
            'flight_no': self.flight_no,
            'sign_date': self.sign_date,
            'departure_1': self.departure_1,
            'traffic_type': self.traffic_type,
            'permission_no': self.permission_no,
            'airoperator_name': self.airoperator_name,
            'place_of_business': self.place_of_business,
            'arrival_1_date_time': self.arrival_1_date_time,
            'departure_1_date_time': self.departure_1_date_time,
        }

    def get_air_operator_name(self):
        return self.airoperator_name