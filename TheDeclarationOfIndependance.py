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


# Gas Level Function
def gasLevelGauge():
    gasLevelList = ["Empty","Low","Quarter Tank","Half Tank","Three Quarter Tank","Full Tank"]

    currentGasLevel = random.choice(gasLevelList)
    return currentGasLevel


print(gasLevelGauge())








