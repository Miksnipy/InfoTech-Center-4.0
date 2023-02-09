# programmer: Roman Cleary
# date:2.8.2023
# Program: Weather System Updates

#Import Libraries here
import random

#Create weather condition in a list and choose it randomly
def weather():
	weatherForcast = ["Snowing", "Blizerd","Raining","Foggy","Windy","Icy", "Sunshine"]
	weatherCondiction = random.choice(weatherForcast)
	return weatherCondiction

#vaeibal to call weather() once in our VRS()
weatherAlert = weather()

print(weatherAlert)

#VRS() to respond to weather condition
def vehicleResponseSystem():
	print("hellllllllllllllllllooooooooooooooooowwwwwwwwwwwwwwww")