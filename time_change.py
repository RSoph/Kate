cities = {'New York':-5,'San Francisco':-8,'PortlandOR':-8,'PortlandME':-5,'London':0,'Chicago':-6,'Denver':-7,'Paris':1}

from time import time, gmtime, strftime

def Time_Change(location):
	hour = int(strftime('%H', gmtime()) + cities[location]
	if hour <= 0:
		hour += 24
	Time = str(hour) + ':' + strftime('%M', gmtime())
	return Time
	
location = raw_input("What city are you in? ")

if location == "Portland":
	state = raw_input("Which one did you mean? Type OR or ME ")
	if state == "OR":
		print "The local time is " + Time_Change('PortlandOR')
	if state == "ME":
		print "The local time is " + Time_Change('PortlandME')
else:		
	print "The local time is " + str(Time_Change(location))
