from folium import Map, Marker, Icon, Popup
from geo import Geopoint

# Get latitude and Longitude values
latitude = 35.67
longitude = 139.65


#Folium Map instance
mymap = Map(location = [latitude, longitude])


# Create a Geopoint instance
geopoint = Geopoint(latitude, longitude)
weather = geopoint.get_weather()
html = """<div style="width: 200px; display: flex; flex-direction: column">"""

for hourly in weather:
    html += f"""
        <div style="border-bottom: 1px solid black; display:flex; align-items:center">
            <h2 style="padding:0;margin:0">{hourly[0][-8:-6]}H {round(hourly[1])}&deg;</h2>
            <img src="http://openweathermap.org/img/wn/{hourly[3]}@2x.png" style="width: 50px">
        </div>
    """
    
html += "</div>"
    

pop_up = Popup(html= html)
pop_up.add_to(geopoint)
geopoint.add_to(mymap)
                    


#Marker instance
#Marker(location=[latitude, longitude], popup="<i style='color: blue'>I'm here!!</i>", icon=Icon(color="green", icon="info-sign")).add_to(mymap)

# Save the Map instance into a HTML file
mymap.save("map.html")