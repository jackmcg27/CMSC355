#***********************************************************
# Currency Module
#
# Component: Task Layer - Currency Service
#***********************************************************
# Function:
#       Display the available currencies along with the exchange rate for the current currency to the others. 
#       When the currency is changed, then all prices on other screens will be displayed in the desiredCured currency
#***********************************************************
# Input:
#       Parameters - params - list containing 3 elements
#                             element 0 -> amount to be exchanged
#                             element 1 -> Currency that the amount is in (from currency)
#                             element 2 -> Currency to be exchanged to (desired currency)
# Output:
#       Return - returnCode -> 0 if the currency was found, -1 otherwise
#***********************************************************
# Author: Jack McGowan
# Version: 4/19/2023 CMSC 355
#***********************************************************

import config
import csv
import utility_layer

def changeCurrency(params):
    if len(params) != 3:
        utility_layer.errorHandler('803')
        return -1
    amount = float(params[0])
    fromCur = params[1]
    desiredCur = params[2]
#--------------------------------------------------------
# Open the file containing the available currencies and read them in to the rows variable
#--------------------------------------------------------
    with open(config.currencyFileName, 'r') as file:
        csvreader = csv.reader(file)
        rows = [] # Holds the list of currencies
        for row in csvreader:
            rows.append(row)
        rows.pop(0) # Remove the headers from the list
        n = len(rows) # Store the number of available currencies
#--------------------------------------------------------
# If the desiredCur is within the number of currencies then it exists and can be selected
# else, there is no currency at that index and call the errorHandler
#--------------------------------------------------------
    fromCurIndex = -1
    desiredCurIndex = -1
    for i in range(n):
        if fromCur.lower() == rows[i][0]:
            fromCurIndex = i
        if desiredCur.lower() == rows[i][0]:
            desiredCurIndex = i
    if fromCurIndex == -1 or desiredCurIndex == -1:
        utility_layer.errorHandler('805')
        return -1
    exchangedAmount = amount * float(rows[desiredCurIndex][1])
    print(f"{rows[fromCurIndex][2]}{round(float(amount),2):#.2f} ----> {rows[desiredCurIndex][2]}{round(exchangedAmount * (float(rows[desiredCurIndex][1]) / float(rows[fromCurIndex][1])),2):#.2f}")
    return 0