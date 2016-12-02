from geopy.geocoders import Nominatim 
from geopy.distance import vincenty

import sys
reload(sys)
sys.setdefaultencoding('utf-8')



def flush():
	sys.stdout.flush()

print '---------Welcome to the 7 Wonders of the World distance calculator--------- \n \nWe calculate out your distance from anywhere in the world to the seven wonders of the world \n \nWhen prompted please enter your town followed by your country \n\nIn the format "Highlands Ranch USA"\n \nNow please enter a Location: '

flush()

user_location = raw_input()

geolocator = Nominatim()

#print  (user_location)

location = geolocator.geocode(user_location)

print('\nYour entered location: ' )
print(location.address)

flush()

user_coordinates = (location.latitude, location.longitude)

#print(a)

petra_location = geolocator.geocode("Petra, Jordan")
petra = (petra_location.latitude, petra_location.longitude)
petra_distance = (vincenty(user_coordinates, petra).miles)

CI_location = geolocator.geocode("Chichen Itza, Mexico")
chichen_itza = (CI_location.latitude, CI_location.longitude)
chichen_itza_distance = (vincenty(user_coordinates, chichen_itza).miles)

TC_location = geolocator.geocode("The Colosseum, Italy")
the_colosseum = (TC_location.latitude, TC_location.longitude)
the_colosseum_distance = (vincenty(user_coordinates, the_colosseum).miles)

GWOC_location = geolocator.geocode("Christ the Redeemer, Brazil")
great_wall_of_china = (GWOC_location.latitude, GWOC_location.longitude)
great_wall_of_china_distance = (vincenty(user_coordinates, great_wall_of_china).miles)

TM_location = geolocator.geocode("Taj Mahal, India")
taj_mahal = (TM_location.latitude, TM_location.longitude)
taj_mahal_distance = (vincenty(user_coordinates, taj_mahal).miles)


CTR_location = geolocator.geocode("Christ the Redeemer, Brazil")
christ_the_redeemer = (CTR_location.latitude, CTR_location.longitude)
christ_the_redeemer_distance = (vincenty(user_coordinates, christ_the_redeemer).miles)

MP_location = geolocator.geocode("Macchu Picchu, Peru")
macchu_picchu = (MP_location.latitude, MP_location.longitude)
macchu_picchu_distance = (vincenty(user_coordinates, macchu_picchu).miles)

all_values = [petra_distance, christ_the_redeemer_distance, macchu_picchu_distance, the_colosseum_distance, taj_mahal_distance, great_wall_of_china_distance, chichen_itza_distance]

x = 1000000000000000000000000.001

for i in all_values:
	if i < x:
		x = i
	if x == petra_distance:
		lowest_location = "Petra"
	if x == great_wall_of_china_distance:
		lowest_location = "Great Wall of China"
	if x == the_colosseum_distance:
		lowest_location = "Colosseum"
	if x == christ_the_redeemer_distance:
		lowest_location = "Christ the Redeemer"
	if x == taj_mahal_distance:
		lowest_location = "Taj Mahal"
	if x == macchu_picchu_distance:
		lowest_location = "Macchu Picchu"
	if x == chichen_itza_distance:
		lowest_location = "Chichen Itza"

print "\nThe lowest value is", x, "miles, making the wonder closest to you the", lowest_location


flight_time = x / 570  

print "\nThe average amount of time it would take you to fly to", lowest_location, "is", flight_time, "hours. \n\n ---------Happy Travels!---------\n"

flush()


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