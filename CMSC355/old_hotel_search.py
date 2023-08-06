#***********************************************************
# Hotels Module
#
# Component: Task Layer - Hotel Search Service
#***********************************************************
# Function:
#       Display the available hotels in order based on the sorting method provided by the user (Star rating or price per night)
#***********************************************************
# Input:
#       Parameters - None
# Output:
#       Return - list containing information of hotel booked
#                If no hotel is booked, then returns -1
#***********************************************************
# Author: Jack McGowan
# Version: 4/19/2023 CMSC 355
#***********************************************************

import config
import csv

#--------------------------------------------------------
# Function to sort the list by star rating
# Parameters: hotelList -> List containing lists with 3 elemets
#             0th element: hotel name 
#             1st element: Star rating out of 5
#             2nd element: price per night
# Returns: List sorted by star rating
#--------------------------------------------------------
def sortStarRating(hotelList):
    n = len(hotelList) # store number of hotels
    # For loop to sort the list by the 1st element, star rating
    for i in range(n):
        for j in range(n - i - 1):
            if float(hotelList[j][1]) < float(hotelList[j + 1][1]):
                hotelList[j], hotelList[j+1] = hotelList[j+1], hotelList[j]
    return hotelList

#--------------------------------------------------------
# Function to sort the list by price per night
# Parameters: hotelList -> List containing lists with 3 elemets
#             0th element: hotel name 
#             1st element: Star rating out of 5
#             2nd element: price per night
# Returns: List sorted by price per night
#--------------------------------------------------------
def sortPrice(hotelList):
    hotelList.sort(key=lambda x:int(x[2])) # Sort list by price per night (2nd element)
    return hotelList

#--------------------------------------------------------
# Function display and choose a hotel to book
# Parameters: None
# Returns: info on hotel booked if successful
#          -1 if no hotel booked
#--------------------------------------------------------
def hotelSearch():
    # Display options to sort by
    print("How would you like to sort the hotels?")
    print("1. Star rating")
    print("2. Price per night")
    print("Enter 0 to return to the main menu")
    select = -1 # Initialize select variable to hold user input
    # While the input is not a valid option, continue to prompt and read user input
    while select not in ['0','1','2']:
        select = input("Your selection: ")
    if select == '0':
        print("Returning to main menu\n\n\n\n")
        return -1
    print("\n\n")
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
# 1 means star rating, 2 means price
#-----------------------------------------------------
    if select == '1':
        hotelList = sortStarRating(hotelList)
    elif select == '2':
        hotelList = sortPrice(hotelList)
#-----------------------------------------------------
# Display all of the available hotels
# Format: {index number}. {hotel name} {star rating}/5 {price}
# For the currency, multiply the stored value by the multiplier of the current currency
#-----------------------------------------------------
    for i in range(n):
        print(f"{i}. {hotelList[i][0]} {hotelList[i][1]}/5 {config.curCurrency[2]}{round(float(hotelList[i][2]) * float(config.curCurrency[1]), 2):#.2f}")
    select = input("Select a hotel to book or enter any letter to cancel: ")
#-----------------------------------------------------
# If the input is a number that is within the number of hotels, book the hotel
# else, return to main menu
#-----------------------------------------------------
    if select.isnumeric() and int(select) < n:
        select = int(select)
        print(f"You have booked the {hotelList[select][0]} for {config.curCurrency[2]}{round(float(hotelList[select][2]) * float(config.curCurrency[1]), 2):#.2f}\n\n\n\n")
        return hotelList[select]
    else:
        print(f"No hotel booked\nReturning to main menu\n\n\n\n")
        return -1
        
