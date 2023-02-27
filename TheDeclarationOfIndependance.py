# Programmer: Roman Cleary
# Date:2.15.2023
# Program: Infotech center 4.0 -Restaurants



"""
We will create a function that will tell us the closest Restaurant
    - create a list of Restaurant
"""
import random
import sleep

def listOfRestaurants():
    restaurants = ["Applebee","Outback","Red Lobster","Denny's","Cracker Barrel","Wendys","KFC","Subway",,"Burger Kings","Arbys"]
    restaurantsNearby = random.choice( restaurants)
    return restaurantsNearby

 restaurantList = listOfRestaurants()


def  restaurantsfood():
    milesToRestaurants = round(random.uniform(26,50),2)
if  restaurantList == "Applebee":
    print("\nThis is a close Restaurant", listOfRestaurants(),"which is",milesToRestaurants,"miles away.")
    sleep(1.5)
