import sys
def serviceBroker(argv):
    foundService = False # Initialize flag to determine when a service is found
    serviceCode = argv[0] # Store the service code to look for
    serviceParams = argv[1:]
    print(serviceCode + "\n")
    print(serviceParams)

if __name__ == "__main__":
    serviceBroker(sys.argv[1:])