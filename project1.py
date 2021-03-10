from folium import Map, Marker
 

latitude = float("40.09")
longitude = float("-3.47")


antipode_latitude = latitude.__mul__(int("-1"))

if longitude.__lt__(float("0")) and longitude.__gt__(float("-180")):
    print(longitude.__gt__(float('-180')))
    antipode_longitude = longitude.__add__(float("180"))
elif longitude.__eq__(float("0")):
    antipode_longitude = float("180")
elif longitude.__gt__(float("180")) or longitude.__lt__(float("-180")):
    antipode_longitude = str(f"Error {longitude}: check number")
else:
    antipode_longitude = longitude.__sub__(float("180"))
location = list((antipode_latitude, antipode_longitude))
mymap = Map(location)
Marker(location, popup=str("<i>My Antipode</i>")).add_to(mymap)

mymap.save(str("antipode.html"))


print(antipode_latitude, antipode_longitude)
print(mymap)

