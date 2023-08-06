import currency_exchange
import config

def main():
    print("Testing call to currency_exchange with 3")
    data = currency_exchange.changeCurrency()
    print(f"Returned data: {data}\n")
    print(f"Checking value of curCurrnecy: {config.curCurrency}")
    print("Testing call to currency_exchange with 5 (out of range)")
    data = currency_exchange.changeCurrency()
    print(f"Returned data: {data}")
    print(f"Checking value of curCurrnecy: {config.curCurrency}")

if __name__ == "__main__":
    main()