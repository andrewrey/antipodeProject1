from folium import Map, Marker
from geo import Geopoint
 
# Get Latitude and Longitude. As well set the tool tip message.
latitude = 40.09
longitude = -3.47
tool_tip = "Click Me!!"

# reverse the latitude to the opposite
antipode_latitude = latitude * -1 

# Logice for reversing Longitude: -180 if postive, +180 if negative
if longitude < 0.0 and longitude > -180.0:
    antipode_longitude = longitude + 180.0
elif longitude == 0.0:
    antipode_longitude = 180.0
elif longitude > 180.0 or longitude < -180.0:
    antipode_longitude = f"Error {longitude}: check number"
else:
    antipode_longitude = longitude - 180.0
    
# create a list of the antipodes for Lat and Long    
location = [antipode_latitude, antipode_longitude]

# Create the Map using Stamen Terrain, add location marker and popup with tooltip
mymap = Map(location,tiles="Stamen Terrain")
Marker(location, popup=f"<i>My Antipode: Latitude {antipode_latitude} Longitude {antipode_longitude} </i>", tooltip=tool_tip).add_to(mymap)

# Save map to file
mymap.save("antipode2.html")

mypoint = Geopoint(41.2, 4.1)
print(mypoint.closest_parallel())
print(mypoint.latitude)


print(antipode_latitude, antipode_longitude)
print(mymap)