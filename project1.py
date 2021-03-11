from folium import Map, Marker
 
# Get Latitude and Longitude. As well set the tool tip message.
latitude = float("40.09")
longitude = float("-3.47")
tool_tip = str("Click Me!!")

# reverse the latitude to the opposite
antipode_latitude = latitude.__mul__(int("-1"))

# Logice for reversing Longitude: -180 if postive, +180 if negative
if longitude.__lt__(float("0")) and longitude.__gt__(float("-180")):
    print(longitude.__gt__(float('-180')))
    antipode_longitude = longitude.__add__(float("180"))
elif longitude.__eq__(float("0")):
    antipode_longitude = float("180")
elif longitude.__gt__(float("180")) or longitude.__lt__(float("-180")):
    antipode_longitude = str(f"Error {longitude}: check number")
else:
    antipode_longitude = longitude.__sub__(float("180"))
    
# create a list of the antipodes for Lat and Long    
location = list((antipode_latitude, antipode_longitude))

# Create the Map using Stamen Terrain, add location marker and popup with tooltip
mymap = Map(location,tiles="Stamen Terrain")
Marker(location, popup=str(f"<i>My Antipode: Latitude {antipode_latitude} Longitude {antipode_longitude} </i>"), tooltip=tool_tip).add_to(mymap)

# Save map to file
mymap.save(str("antipode.html"))


print(antipode_latitude, antipode_longitude)
print(mymap)

