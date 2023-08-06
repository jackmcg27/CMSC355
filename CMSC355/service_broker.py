#***********************************************************
# service_broker Module
#
# Component: Orchestration Layer
#***********************************************************
# Function:
#       Determine what service was requested and call the required function to perform the service
#***********************************************************
# Input:
#       Parameters - serviceCode -> Code of the requested service (string)
# Output:
#       Return - returnCode -> 0 if service was found, -1 if not
#                returnedData -> Data from the service that was called
#***********************************************************
# Author: Jack McGowan
# Version: 4/19/2023 CMSC 355
#***********************************************************

import config
import utility_layer
import csv
import sys

#--------------------------------------------------------
# Function to determine what service was called and call the service
# Parameters: argv -> arguments come from command line
# Returns: returnedData -> Data returned from the service
#          returnCode -> 0 if service was called successfully, -1 otherwise
#--------------------------------------------------------
def serviceBroker(argv):
    foundService = False # Initialize flag to determine when a service is found
    serviceCode = argv[0] # Store the service code to look for
    serviceParams = argv[1:] # Store the remaining parameters
#-----------------------------------------------------
# Open the file containing the service information and parse it into rows
#-----------------------------------------------------
    with open(config.serviceFileName, 'r') as file:
        csvreader = csv.reader(file)
        rows = []
        for row in csvreader:
            rows.append(row)
        rows.pop(0) # Remove the 0th element since it contains headers
    i = 0
    curService = rows[i][0] # set the current service to the 0th element of the first list
#-----------------------------------------------------
# While the foundService flag is false and i is less than the number of services, continue
#-----------------------------------------------------
    while foundService == False and i <= len(rows):
#-----------------------------------------------------
# Check to see if the curService is equal to the requested serviceCode
# if it is, set the foundService flag to True
# If it is not, if i is less than the number of services, set curService to the next service number
#-----------------------------------------------------
        if curService == serviceCode:
            foundService = True
            #-----------------------------------------------------
            # If i is not 0, set the serviceIndex to i - 1, else serviceIndex = 0
            # This is for the way the loop is constructed and allows for the service numbers to be
            # out of order as well as not continuous. serviceIndex is the index needed to access the
            # service module and function later
            #-----------------------------------------------------
            if i != 0:
                serviceIndex = i - 1
            else:
                serviceIndex = 0
        else:
            if i < len(rows):
                curService = rows[i][0]
            i += 1
#-----------------------------------------------------
# If the foundService flag is True, import the module of the requested service
# Set serviceFunc to the name of the function of the service requested
# Set func to the function in the module
# Call the service and store results in returnedData
# If foundService flag is False, call the errorHandler and return -1
#-----------------------------------------------------
    if foundService is True:
        module = __import__(rows[serviceIndex][2])
        serviceFunc = rows[serviceIndex][3]
        func = getattr(module, serviceFunc)
        returnedData = func(serviceParams)
        returnCode = 0
    else:
        utility_layer.errorHandler('703')
        returnCode = returnedData = -1
    return returnCode, returnedData

if __name__ == "__main__":
    serviceBroker(sys.argv[1:])