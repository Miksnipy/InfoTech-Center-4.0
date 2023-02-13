# programmer: Roman Cleary
# date:2.8.2023
# Program: Weather System Updates

#Import Libraries here
import random

#Create weather condition in a list and choose it randomly
def weather():
	weatherForcast = ["Snowing", "Blizerd","Rain","Foggy","Windy","Icy", "Sunshine"]
	weatherCondiction = random.choice(weatherForcast)
	return weatherCondiction

#vaeibal to call weather() once in our VRS()
weatherAlert = weather()



print(weatherAlert)

#VRS() to respond to weather condition
def vehicleResponseSystem():
	if weatherAlert == "Snowing":
		print("\nNWS has changed your alarm by 15 minutes because of the waether forcast of", weatherAlert)
		print("VRS has been engaged only allowing your vehicle to go 45 MPH")
	elif weatherAlert == "Blizerd":
		print("\nNWS has changed your alarm by 30 minutes because of the waether forcast of", weatherAlert)
		print("VRS has been engaged only allowing your vehicle to go 35 MPH")
	elif weatherAlert == "Rain":
		print("\nNWS has not changed your alarm ", weatherAlert)
		print("VRS has not been engaged ")
	elif weatherAlert == "Foggy":
		print("\nNWS has not changed your alarm ", weatherAlert)
		print("VRS has not been engaged ")
	elif weatherAlert == "Windy":
		print("\nNWS has not changed your alarm ", weatherAlert)
		print("VRS has not been engaged")
	elif weatherAlert == "Icy":
		print("\nNWS has changed your alarm by 45 minutes because of the waether forcast of", weatherAlert)
		print("VRS has been engaged only allowing your vehicle to go 25 MPH")
	else:
		print("\nNWS has not changed your alarm ", weatherAlert)
		print("VRS has not been engaged ")



vehicleResponseSystem()