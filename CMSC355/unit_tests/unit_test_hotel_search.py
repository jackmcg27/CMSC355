import hotel_search

def main():
    print("Testing call to hotel search and sorting by departure time")
    data = hotel_search.hotelSearch(['stars'])
    print(f"Returned data: {data}\n")
    print("Testing call hotel search and sorting by price")
    data = hotel_search.hotelSearch(['price'])
    print(f"Returned data: {data}")

if __name__ == "__main__":
    main()