from geopy.geocoders import Nominatim 
from geopy.distance import vincenty


user_location = raw_input('Enter A Location: ')

geolocator = Nominatim()

#print  (user_location)

location = geolocator.geocode(user_location)

#print(location.address)

a = (location.latitude, location.longitude)

#print(a)

user_coordinates = a
petra = (30.3285, 35.4444)
petra_distance = (vincenty(user_coordinates, petra).miles)

print 'Your Distance from Petra is', petra_distance,  'miles.' 








































#geolocator = Nominatim()
# location = geolocator.geocode("Newport Rhode Island")
# print(location.address)
# a = (location.latitude, location.longitude)

# location2 = geolocator.geocode("Cleveland Ohio")
# print(location2.address)
# b = (location2.latitude, location2.longitude)

# newport_ri = a
# cleveland_oh = b
# print(vincenty(newport_ri, cleveland_oh).miles)