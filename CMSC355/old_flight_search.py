#***********************************************************
# Flights Module
#
# Component: Task Layer - Flight Search Service
#***********************************************************
# Function:
#       Display the available flights in order based on the sorting method provided by the user (Departure time or price)
#***********************************************************
# Input:
#       Parameters - None
# Output:
#       Return - list containing information of flight booked
#                If no flight is booked, then returns -1
#***********************************************************
# Author: Jack McGowan
# Version: 4/19/2023 CMSC 355
#***********************************************************

import config
import csv

#--------------------------------------------------------
# Function to sort the list by departure time
# Parameters: flightList -> List containing lists with 4 elemets
#             0th element: airline 
#             1st element: hour of departure in 24 hour format
#             2nd element: minutes of departure
#             3rd element: price
# Returns: List sorted by departure time
#--------------------------------------------------------
def sortDepartureTime(flightList):
    n = len(flightList) # store number of flights
    flightList.sort(key=lambda x:int(x[1])) # Sort the list based on the hours (smallest to greatest)
    # For loop to sort the list by the minutes
    for i in range(n):
        for j in range(n - i - 1):
            if flightList[j][1] == flightList[j+1][1]: # Do not sort unless the hour is the same
                if int(flightList[j][2]) > int(flightList[j+1][2]):
                    flightList[j], flightList[j+1] = flightList[j+1], flightList[j]
    return flightList

#--------------------------------------------------------
# Function to sort the list by price
# Parameters: flightList -> List containing lists with 4 elemets
#             0th element: airline 
#             1st element: hour of departure in 24 hour format
#             2nd element: minutes of departure
#             3rd element: price
# Returns: List sorted by departure time
#--------------------------------------------------------
def sortPrice(flightList):
    flightList.sort(key=lambda x:x[3]) # Sort based on the 3rd element in the list
    return flightList

#--------------------------------------------------------
# Function to display and choose a flight to book
# Parameters: None
# Returns: info on flight booked if successful
#          -1 if no flight booked
#--------------------------------------------------------
def flightSearch():
    # Display options to sort by
    print("How would you like to sort the flights?")
    print("1. Departure time")
    print("2. Price")
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
# Open the file containing the flight information and parse it into flightList
#-----------------------------------------------------
    with open(config.flightFileName, 'r') as file:
        csvreader = csv.reader(file)
        flightList = []
        for row in csvreader:
            flightList.append(row)
        flightList.pop(0) # Remove the 0th element since it contains headers
    n = len(flightList) # Store the number of flights stored
#-----------------------------------------------------
# Determine if the list should be sorted by departure time or price
# 1 means departure time, 2 means price
#-----------------------------------------------------
    if select == '1':
        flightList = sortDepartureTime(flightList)
    elif select == '2':
        flightList = sortPrice(flightList)
    # These variables are for displaying the correct times
    x = 'pm'
    y = 'am'
    print("Your flight options:")
#-----------------------------------------------------
# Display all of the available flights
# Format: {index number}. {airline} {departure hours}:{departure minutes}{am or pm} {price}
# There is conditional formatting to determine if it is am or pm and to convert the 24 hour format to 12 hour format
# If hour is 0, add 12 to get to 12am
# If hour is less than 13 and not 0, display hour
# If hour is greater than 12, subtract 12 and display
# If hour is 12 or lower, display am
# If hour is greater than 12, display pm
# For the currency, multiply the stored value by the multiplier of the current currency
#-----------------------------------------------------
    for i in range(n):
        print(f"{i}. {flightList[i][0]} {(int(flightList[i][1]) + 12 if flightList[i][1] == 0 else flightList[i][1]) if int(flightList[i][1]) < 13 else int(flightList[i][1]) - 12}:{int(flightList[i][1]):02d}{x if int(flightList[i][1]) >= 12 else y} {config.curCurrency[2]}{round(float(flightList[i][3]) * float(config.curCurrency[1]), 2):#.2f}")
    select = input("Select a flight to book or enter any letter to cancel: ") # Get input from user
#-----------------------------------------------------
# If the input is a number that is within the number of flights, book the flight
# else, return to main menu
#-----------------------------------------------------
    if select.isnumeric() and int(select) < len(flightList):
        select = int(select)
        print(f"You have booked the flight from {flightList[select][0]} at {(int(flightList[select][1]) + 12 if flightList[select][1] == 0 else flightList[select][1]) if int(flightList[select][1]) < 13 else int(flightList[select][1]) - 12}:{int(flightList[select][1]):02d}{x if int(flightList[select][1]) >= 12 else y} for {config.curCurrency[2]}{round(float(flightList[select][3]) * float(config.curCurrency[1]), 2):#.2f}\n\n\n\n")
        return flightList[select]
    else:
        print(f"No flight booked\nReturning to main menu\n\n\n\n")
        return -1