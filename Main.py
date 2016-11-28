from geopy.geocoders import Nominatim 
from geopy.distance import vincenty

import sys
reload(sys)
sys.setdefaultencoding('utf-8')



def flush():
	sys.stdout.flush()

print '---------Welcome to the 7 Wonders of the World distance calculator--------- \n \nWe calculate out your distance from anywhere in the USA to the seven wonders of the world \n \nWhen prompted please enter your Zip code followed by a comma and your 2 letter state acronym \n\nIn the format "80129, CO"\n \n Now please enter a Location: '

flush()

user_location = raw_input()

geolocator = Nominatim()

#print  (user_location)

location = geolocator.geocode(user_location)

print('Your entered location: ' )
print(location.address)

flush()

user_coordinates = (location.latitude, location.longitude)

#print(a)


petra = (30.3285, 35.4444)
petra_distance = (vincenty(user_coordinates, petra).miles)

chichen_itza = (20.6843, 88.5678)
chichen_itza_distance = (vincenty(user_coordinates, chichen_itza).miles)

the_colosseum = (41.8902, 12.4922)
the_colosseum_distance = (vincenty(user_coordinates, the_colosseum).miles)

great_wall_of_china = (40.4319, 116.5704)
great_wall_of_china_distance = (vincenty(user_coordinates, great_wall_of_china).miles)

taj_mahal = (27.1750, 78.0422)
taj_mahal_distance = (vincenty(user_coordinates, taj_mahal).miles)

christ_the_redeemer = (22.9519, 43.2105)
christ_the_redeemer_distance = (vincenty(user_coordinates, christ_the_redeemer).miles)

macchu_picchu = (20.6843, 88.5678)
macchu_picchu_distance = (vincenty(user_coordinates, macchu_picchu).miles)

print '\nYour Distance from Petra is', petra_distance,  'miles.\n' 
print 'Your Distance from Chichen Itza is', chichen_itza_distance, 'miles.\n'
print 'Your Distance from The Colosseum is', the_colosseum_distance, 'miles.\n'
print 'Your Distance from The Great Wall of China is', great_wall_of_china_distance, 'miles.\n'
print 'Your Distance from The Taj Mahal is', taj_mahal_distance, 'miles.\n'
print 'Your Distance from Christ the Redeemer is', christ_the_redeemer_distance, 'miles.\n'
print 'Your Distance from Macchu Picchu is', macchu_picchu_distance, 'miles.\n'
# flush()







































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