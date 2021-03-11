import datetime as dt
from pytz import timezone
from timezonefinder import TimezoneFinder


class Geopoint:
    
    def __init__(self,latitude, longitude):
        self.latitude = latitude
        self.longitude = longitude
        
    def closest_parallel(self):
        return round(self.latitude)
    
    def get_time(self):
        tf = TimezoneFinder()
        time_zone_string = tf.timezone_at(lat=self.latitude, lng=self.longitude)
        source_date = dt.datetime.now(timezone(f'{time_zone_string}'))
        return source_date

    
        
        
van = Geopoint(49.28, -123.12)

print(van.closest_parallel())

print(van.get_time())