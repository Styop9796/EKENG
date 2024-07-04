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
