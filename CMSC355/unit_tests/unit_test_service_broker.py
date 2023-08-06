import service_broker

def main():
    print("Testing call to service broker with 0")
    data = service_broker.serviceBroker('0')
    print(f"Returned data: {data}\n")
    print("Testing call to service_broker with 5 (out of range)")
    data = service_broker.serviceBroker('5')
    print(f"Returned data: {data}")

if __name__ == "__main__":
    main()