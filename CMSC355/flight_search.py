#***********************************************************
# Flights Module
#
# Component: Task Layer - Flight Search Service
#***********************************************************
# Function:
#       Display the available flights in order based on the sorting method provided by the user (Departure time or price)
#***********************************************************
# Input:
#       Parameters - params - list containing the sort method
# Output:
#       Return - 0 if successful, -1 otherwise 
#***********************************************************
# Author: Jack McGowan
# Version: 4/19/2023 CMSC 355
#***********************************************************

import config
import csv
import utility_layer

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
    flightList = setupFlightTimes(flightList)
    flightList.sort(key=lambda x:int(x[0][0])) # Sort the list based on the hours (smallest to greatest)
    # For loop to sort the list by the minutes
    for i in range(n):
        for j in range(n - i - 1):
            if flightList[j][0][0] == flightList[j+1][0][0]: # Do not sort unless the hour is the same
                if int(flightList[j][0][1]) > int(flightList[j+1][0][1]):
                    flightList[j], flightList[j+1] = flightList[j+1], flightList[j]
    return flightList

#--------------------------------------------------------
# Function to sort the list by price
# Parameters: flightList -> List containing lists with 4 elemets
#             0th element: departure time 
#             1st element: from location
#             2nd element: arival time
#             3rd element: destination location
# Returns: List sorted by departure time
#--------------------------------------------------------
def sortPrice(flightList):
    setupFlightTimes(flightList)
    flightList.sort(key=lambda x:int(x[4])) # Sort based on the 4th element in the list
    return flightList

def setupFlightTimes(flightList):
    n = len(flightList) # store number of flights
    departureList = flightList # departureList is a copy of flightList that will be manipulated
    for i in range(n):
        #------------------------------------------------
        # Manipulating the departure time to make it sortable
        # Spliting it into hours, minutes, am/pm
        #------------------------------------------------
        departureList[i][0] = departureList[i][0].replace(':', ' ').replace('am',' am').replace('pm',' pm')
        departureList[i][0] = departureList[i][0].split()
        #------------------------------------------------
        # If the flight departs in the pm, convert hour to 24 hours base
        # Special case: If it departs between 12pm and 12:59pm, set hour back to 12
        #------------------------------------------------
        if departureList[i][0][2] == 'pm':
            hold = int(departureList[i][0][0]) + 12
            if hold == 24:
                departureList[i][0][0] = 12
            else:
                departureList[i][0][0] = str(hold)
        #------------------------------------------------
        # If the flight departs between 12am and 12:59am, set hour to 0
        #------------------------------------------------
        if departureList[i][0][2] == 'am' and departureList[i][0][0] == '12':
            departureList[i][0][0] = 0
    return departureList

#--------------------------------------------------------
# Function to display and choose a flight to book
# Parameters: params - Method to sort by
# Returns: 0 if successful
#          -1 if unsuccessful
#--------------------------------------------------------
def flightSearch(params):
    if len(params) == 0:
        utility_layer.errorHandler('610')
        return -1 
    sortMethod = params[0] # Store sort method in sortMethod
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
# time means departure time, price means price
#-----------------------------------------------------
    if sortMethod.lower() == 'time':
        flightList = sortDepartureTime(flightList)
    elif sortMethod.lower() == 'price':
        flightList = sortPrice(flightList)
    else:
        utility_layer.errorHandler('614')
        return -1
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
        holdDepartureLocation = flightList[i][1].split()
        holdArrivalLocation = flightList[i][3].split()
        print(f"{i}. {(int(flightList[i][0][0]) + 12 if flightList[i][0][0] == 0 else flightList[i][0][0]) if int(flightList[i][0][0]) < 13 else int(flightList[i][0][0]) - 12}:{flightList[i][0][1]}{flightList[i][0][2]} {holdDepartureLocation[0]}, {holdDepartureLocation[1]} ---> {flightList[i][2]} {holdArrivalLocation[0]}, {holdArrivalLocation[1]} {config.curCurrency[2]}{round(float(flightList[i][4]) * float(config.curCurrency[1]), 2):#.2f}")
    return 0 # 0 means success