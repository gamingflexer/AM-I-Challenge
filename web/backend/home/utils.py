from geopy.geocoders import Nominatim
 
geolocator = Nominatim(user_agent="geoapiExercises")
 
def location_finder(lat, lng):
    try:
        lat = str(lat)
        lng = str(lng)
        location = geolocator.geocode(lat+","+lng)
        if location != None:
            location_split = location.address.split(',')
            location_shortened = location_split[0]+","+location_split[1]+","+location_split[2]
            return location_shortened
        else:
            return "Not Found"
    except Exception as e:
        print(e)
        return "Not Found"