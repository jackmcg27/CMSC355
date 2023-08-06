import flight_search

def main():
    print("Testing call to flight search and sorting by departure time")
    data = flight_search.flightSearch()
    print(f"Returned data: {data}\n")
    print("Testing call flight search and sorting by price")
    data = flight_search.flightSearch()
    print(f"Returned data: {data}")
    print("Testing call to flight module and choosing 0 to return to main menu")
    data = flight_search.flightSearch()
    print(f"Returned data: {data}")
    print("Testing call to flight module and not choosing a flight to return to main menu")
    data = flight_search.flightSearch()
    print(f"Returned data: {data}")

if __name__ == "__main__":
    main()