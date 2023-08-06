#***********************************************************
# Utility Module
#
# Component: Utility Layer
#***********************************************************
# Function:
#       Display the available flights in order based on the sorting method provided by the user (Departure time or price)
#***********************************************************
# Input:
#       Parameters - errorCode: Numerical code that corresponds to an error message
# Output:
#       Return - Prints error message to screen
#***********************************************************
# Author: Jack McGowan
# Version: 4/19/2023 CMSC 355
#***********************************************************

import csv
import config

def errorHandler(errorCode):
#--------------------------------------------------------
# Try to open the file containing error messages of the current language
# Check the file row by row to determine if the error code is in it
#--------------------------------------------------------
    try:
        with open("data_files/errors_" + config.curLanguage +".csv") as file:
            csvreader = csv.reader(file) #Initializing csvreader to parse file
            for row in csvreader:
#--------------------------------------------------------
# If the 0th element is equal to the error code, print out the 1st element which should be the error message
#--------------------------------------------------------
                if row[0] == errorCode:
                    print(f"{row[1]}")
                    return 0
        
#--------------------------------------------------------
#If the file was not able to be opened, display that is was a failure
#--------------------------------------------------------
    except IOError as e:
        print(f"Error code {errorCode} not found in {e}")
    return -1
    