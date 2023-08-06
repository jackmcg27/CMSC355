import utility_layer

def main():
    print("Testing call to utility layer with 805")
    data = utility_layer.errorHandler('805')
    print(f"Returned data: {data}\n")
    print("Testing call to utility_layer with 1000 (Bad error code)")
    data = utility_layer.errorHandler('1000')
    print(f"Returned data: {data}")

if __name__ == "__main__":
    main()