#***********************************************************
# Language Module
#
# Component: Utility Layer - Error Translator
#***********************************************************
# Function:
#       Change the language that the error messages appear in
#***********************************************************
# Input:
#       Parameters - None
#       Will read in choice of language
# Output:
#       Return - returnCode -> 0 if the language was found, -1 otherwise (Note that the curLanguage variable will be changed)
#***********************************************************
# Author: Jack McGowan
# Version: 4/19/2023 CMSC 355
#***********************************************************
import config
import csv
import utility_layer

def changeLanguage():
    print("Current Language: " + config.curLanguage)
    with open(config.languagesFileName, 'r') as file:
        csvreader = csv.reader(file)
        languages = []
        for row in csvreader:
            languages.append(row)
        n = len(languages)
    for i in range(n):
        print(f"{i}. {languages[i][0]}")
    desiredLang = int(input("Your selection: "))
    returnCode = 0
    if desiredLang < n:
        config.curLanguage = languages[desiredLang][1]
    else:
        utility_layer.errorHandler('901')
        returnCode = -1
    print("Returing to main menu\n\n\n\n")
    return returnCode

