# programmer: Roman Cleary
# date:1.20.2023
# Program: Infotech center upgrades


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

# Import Libraries Here
import random
from time import sleep

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
gasLevelAlert()











































































