import datetime as dt
from pytz import timezone
from timezonefinder import TimezoneFinder
from sunnyday import Weather
from config import api_key
from random import uniform

class Geopoint:
    latitude_range = (90,-90)
    longitude_range = (180, -180)
    
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
    
    def get_weather(self):
        weather = Weather(api_key, lat=self.latitude, lon=self.longitude)
        return weather.next_12h_simplified()
    
    @classmethod
    def get_random(cls):
        return cls(latitude=uniform(-90, 90), longitude=uniform(-180, 180))
    
    
        
        
van = Geopoint(49.28, -123.12)
random_point = Geopoint.get_random()
print(random_point)

print(van.closest_parallel())

print(van.get_time())
print(van.get_weather())