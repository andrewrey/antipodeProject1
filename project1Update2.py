from folium import Map, Marker, Icon
from geo import Geopoint

# Get latitude and Longitude values
latitude = 40.4
longitude = -3.7


#Folium Map instance
mymap = Map(location = [latitude, longitude])


# Create a Geopoint instance
geopoint = Geopoint(latitude, longitude, popup="Yes, yes it works")
geopoint.add_to(mymap)

#Marker instance
#Marker(location=[latitude, longitude], popup="<i style='color: blue'>I'm here!!</i>", icon=Icon(color="green", icon="info-sign")).add_to(mymap)

# Save the Map instance into a HTML file
mymap.save("map.html")