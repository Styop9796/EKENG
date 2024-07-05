from datetime import datetime

def parse_datetime(date_time):
    try:
        # Attempt to parse with '%d-%m-%Y %H:%M:%S'
        d_time=datetime.strptime(str(date_time), '%Y-%m-%d %H:%M:%S')
        return d_time
    except ValueError:
        try:
            # Attempt to parse with '%d/%m/%Y %H:%M'
            d_time=datetime.strptime(str(date_time), '%d-%m-%Y %H:%M:%S')
            return d_time
        except ValueError:
            # Handle case where date_str does not match either format
            raise ValueError(f"Date '{date_time}' does not match expected formats.")



def categorize_flights(flights):
    armenian_airports = ['EVN','LWN']
    data = {'to_arm': [],
                         'from_arm': [],
                         'in_arm': []}
    for flight in flights:
        if flight.arrival_1 in armenian_airports and flight.departure_1 not in armenian_airports:
            data['to_arm'].append(flight.to_dict())
        elif flight.arrival_1 not in armenian_airports and flight.departure_1 in armenian_airports:
            data['from_arm'].append(flight.to_dict())
        elif flight.arrival_1 in armenian_airports and flight.departure_1 in armenian_airports:
            data['in_arm'].append(flight.to_dict())
    return data



def filter_permission_numbers(data):
    permissions_dict={}
    for item in data:
        permissions_dict[item.permission_no]=str(item.sign_date)
    return permissions_dict