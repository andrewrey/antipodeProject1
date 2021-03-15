from folium import Map, Marker, Icon, Popup
from geo import Geopoint

# Get latitude and Longitude values
latitude = 40.4
longitude = -3.7


#Folium Map instance
mymap = Map(location = [latitude, longitude])


# Create a Geopoint instance
geopoint = Geopoint(latitude, longitude)
pop_up = Popup(html='<h2 style="color:blue">{}</h2>'.format(geopoint.get_weather()[0][2]))
pop_up.add_to(geopoint)
geopoint.add_to(mymap)
                    


#Marker instance
#Marker(location=[latitude, longitude], popup="<i style='color: blue'>I'm here!!</i>", icon=Icon(color="green", icon="info-sign")).add_to(mymap)

# Save the Map instance into a HTML file
mymap.save("map.html")