#***********************************************************
# Hotels Module
#
# Component: Task Layer - Hotel Search Service
#***********************************************************
# Function:
#       Display the available hotels in order based on the sorting method provided by the user (Star rating or price per night)
#***********************************************************
# Input:
#       Parameters - params - list containing the sort method
# Output:
#       Return - 0 if successful, -1 otherwise
#***********************************************************
# Author: Zachary Edicola
# Version: 4/20/2023 CMSC 355
#***********************************************************

import config
import csv
import utility_layer

#--------------------------------------------------------
# Function to sort the list by star rating
# Parameters: hotelList -> List containing lists with 3 elemets
#             0th element: city,country
#             1st element: hotel name 
#             2nd element: Star rating out of 5
#             3rd element: price per night
# Returns: List sorted by star rating
#--------------------------------------------------------
def sortStarRating(hotelList):
    n = len(hotelList) # store number of hotels
    # For loop to sort the list by the 1st element, star rating
    for i in range(n):
        for j in range(n - i - 1):
            if float(hotelList[j][2]) < float(hotelList[j + 1][2]):
                hotelList[j], hotelList[j+1] = hotelList[j+1], hotelList[j]
    return hotelList

#--------------------------------------------------------
# Function to sort the list by price per night
# Parameters: hotelList -> List containing lists with 3 elemets
#             0th element: city,country
#             1st element: hotel name 
#             2nd element: Star rating out of 5
#             3rd element: price per night
# Returns: List sorted by price per night
#--------------------------------------------------------
def sortPrice(hotelList):
    hotelList.sort(key=lambda x:int(x[3])) # Sort list by price per night (2nd element)
    return hotelList
#--------------------------------------------------------
# Function display and choose a hotel to book
# Parameters: None
# Returns: info on hotel booked if successful
#          -1 if no hotel booked
#--------------------------------------------------------
def hotelSearch(params):
    if len(params) == 0:
        utility_layer.errorHandler('611')
        return -1 
    sortMethod = params[0] # Store sort method in sortMethod
#-----------------------------------------------------
# Open the file containing the hotel information and parse it into hotelList
#-----------------------------------------------------
    with open(config.hotelFileName, 'r') as file:
        csvreader = csv.reader(file)
        hotelList = []
        for row in csvreader:
            hotelList.append(row)
        hotelList.pop(0) # Remove the 0th element since it contains headers
        n = len(hotelList) # Store the number of hotels available
#-----------------------------------------------------
# Determine if the list should be sorted by star rating or price
# stars means star rating, price means price
#-----------------------------------------------------
    if sortMethod.lower() == 'stars':
        hotelList = sortStarRating(hotelList)
    elif sortMethod.lower() == 'price':
        hotelList = sortPrice(hotelList)
    else:
        utility_layer.errorHandler('614')
        return -1
    print("Your flight options:")
#-----------------------------------------------------
# Display all of the available hotels
# Format: {index number}. {city} {country} {hotel name} {star rating}/5 {price}
# For the currency, multiply the stored value by the multiplier of the current currency
#-----------------------------------------------------
    for i in range(n):
        holdLocation = hotelList[i][0].split()
        print(f"{i}. {holdLocation[0]}, {holdLocation[1]}  {hotelList[i][1]}  {hotelList[i][2]}/5 {config.curCurrency[2]}{round(float(hotelList[i][3]) * float(config.curCurrency[1]), 2):#.2f}")
    return 0 # 0 means success