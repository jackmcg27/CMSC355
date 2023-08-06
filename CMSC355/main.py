import config
import csv
import service_broker
                  
def displayMainMenu():
    print("Welcome to the travel agency! To begin, enter the number of the task you want.")
    with open(config.serviceFileName,'r') as file:
        csvreader = csv.reader(file)
        next(csvreader) # Skip headers
        rows = []
        for row in csvreader:
            print(row[0], row[1])
            rows.append(row)
    
    select = input("Your selection: ")
    print("\n\n\n")
    service_broker.serviceBroker(select)

def main():
    while 1:
        displayMainMenu()

if __name__ == "__main__":
    main()