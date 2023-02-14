# programmer: Roman Cleary
# date merged:2.6.2023
# Program: Infotech center upgrades

"""
Our welcome screen will start our program letting
drivers know that the InfoTech Center 4.0 OS is loading
"""
# Import Libraries Here
import time
import sys
import random
from time import sleep

x=2
a=0

print("\n\n\033[1;33;40mWelcome - Infotech Center 4.0\n")
time.sleep(x)

while x != 20:
    x += 1
    b = ("\033[1;33;40mInfoTech Center OS is Loading" + "." * a)
    a = a + 1
    sys.stdout.write(('\r'+b) )
    time.sleep(0.5)
    if a == 4:
        a = 0
    if x == 20:
        print('\n\033[1;32;40mDone!')
    x += 1
    b = ("\033[1;33;40mInfoTech Center OS is Loading" + "." * a)
    a = a + 1
    sys.stdout.write('\r'+b) # \r prints a carriage return first, so `b` is printed on top of the previous line.
    time.sleep(0.5)
    if a == 4:
        a = 0
    if x == 20:
        print('\n\033[1;32;40mDone!')

while x != 20:
    x += 1
    b = ("\033[1;33;40mInfoTech Center OS is Loading" + "." * a)
    a = a + 1
    sys.stdout.write('\r'+b) # \r prints a carriage return first, so `b` is printed on top of the previous line.
    time.sleep(0.5)
    if a == 4:
        a = 0
    if x == 20:
        print('\n\033[1;32;40mDone!')

"""
We will create a Function that will tell us our Fuel Gauge level
    - Create a List with gas Levels
    - Randomize and choose from the list to determine our gas level

Create a Function to determine our closest Gas Station
    - Create a list of gas stations
    - Randomly choose a gas station from the list

Create a Function to determine our gas levels and closest gas station
    - Print Gas level
    - Print Closest Gas Station
"""



# Gas Level Function
def gasLevelGauge():
    gasLevelList = ["Empty","Low","Quarter Tank","Half Tank","Three Quarter Tank","Full Tank"]

    currentGasLevel = random.choice(gasLevelList) 
    return currentGasLevel

# Variable calling gasLevelGuage function to store its value
gasLevelIndicator = gasLevelGauge()

# List of Gas Stations Function
def listOfGasStation():
    gasStations = ["Shell","Costco","Buckeys","Speedway","7-11","Circkle-k","Meijer","Family Fare"]
    gasStationNearby = random.choice(gasStations)
    return gasStationNearby
# determine gas level & Closest gas station


def gasLevelAlert():


    milesToGasStationLow = round(random.uniform(1, 25), 2)
    milesToGasStationQuartTank = round(random.uniform(26, 50), 2)

    if gasLevelIndicator == "Empty":
        print("***WARNING YOU ARE ON EMPTY***")
        sleep(1)
        print("Calling Emergency Contact")
    elif gasLevelIndicator == "Low":
        print("****Warning*****")
        sleep(1)
        print("Your Gas Level is low checking Google Maps for the closest gas station.")
        sleep(1.5)
        print("The closest gas station is",listOfGasStation(),"which is",milesToGasStationLow, "miles away")

    elif gasLevelIndicator == "Quarter Tank":
        print("****Warning****")
        sleep(1)
        print("Your gas level is at a Quarter Tank and the closest gas station is",listOfGasStation(),"which is",milesToGasStationQuartTank,"miles away")
    elif gasLevelIndicator == "Half tank":
        print("Your gas tank is Half of a tank is full which is plenty of gas to make it to your destinations today.")
    elif gasLevelIndicator == "Three Quarter tank":
        print("Your gas tank is Three Quarter of a tank is full which is plenty of gas to make it to your destinations today.")
    else:
        print("Your gas tank is full which is plenty of gas to make it to your destinations today.")



#Create weather condition in a list and choose it randomly
def weather():
	weatherForcast = ["Snowing", "Blizerd","Rain","Foggy","Windy","Icy", "Sunshine"]
	weatherCondiction = random.choice(weatherForcast)
	return weatherCondiction

#vaeibal to call weather() once in our VRS()
weatherAlert = weather()





#VRS() to respond to weather condition
def vehicleResponseSystem():
	if weatherAlert == "Snowing":
		print("\nNWS has changed your alarm by 15 minutes because of the waether forcast of", weatherAlert)
		print("\nVRS has been engaged only allowing your vehicle to go 45 MPH")
	elif weatherAlert == "Blizerd":
		print("\nNWS has changed your alarm by 30 minutes because of the waether forcast of", weatherAlert)
		print("\nVRS has been engaged only allowing your vehicle to go 35 MPH")
	elif weatherAlert == "Rain":
		print("\nNWS has not changed your alarm ", weatherAlert)
		print("\nVRS has not been engaged ")
	elif weatherAlert == "Foggy":
		print("\nNWS has not changed your alarm ", weatherAlert)
		print("\nVRS has not been engaged ")
	elif weatherAlert == "Windy":
		print("\nNWS has not changed your alarm ", weatherAlert)
		print("\nVRS has not been engaged")
	elif weatherAlert == "Icy":
		print("\nNWS has changed your alarm by 45 minutes because of the waether forcast of", weatherAlert)
		print("\nVRS has been engaged only allowing your vehicle to go 25 MPH")
	else:
		print("\nNWS has not changed your alarm ", weatherAlert)
		print("\nVRS has not been engaged ")




#Call Functions here
print("\nNational Weather survice is checking condiction")
sleep(2)
print(weatherAlert)
vehicleResponseSystem()
sleep(1)
print("\nchecking gas level")
sleep(2)
gasLevelAlert()