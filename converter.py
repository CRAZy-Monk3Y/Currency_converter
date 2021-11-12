# Python program to convert the currency
# of one country to that of another country

# Import the modules needed
import requests
import json
import os
from datetime import datetime


class CurrencyConvertor:
    # empty dict to store the conversion rates
    rates = {}

    def __init__(self, url):
        if os.stat('data.json').st_size == 0:  # Reading json file size to determine loop condition
            data = requests.get(url).json()  # sends get request and returns json format
            with open('data.json', 'w', encoding='utf-8') as f:  # saving fetched data as json for multiple use
                json.dump(data, f, ensure_ascii=False, indent=4)
            # Extracting only the rates from the json data
            self.rates = data["rates"]
        else:
            f = open('data.json', 'r')
            data = json.load(f)
            self.rates = data["rates"]
            timestamp = data["timestamp"]
            self.time = datetime.fromtimestamp(timestamp)
            print("Data Updated on:", self.time)

    # function to do a simple cross multiplication between
    # the amount and the conversion rates
    def convert(self, from_currency, to_currency, amount):
        initial_amount = amount
        if from_currency != 'EUR':
            amount = amount / self.rates[from_currency]

        # limiting the precision to 2 decimal places
        amount = round(amount * self.rates[to_currency], 2)
        print(f'{initial_amount} {from_currency} = {amount} {to_currency}')


# Driver code
if __name__ == "__main__":
    API_KEY = '#EnterYour API Key here. ' # To get API Key go to https://fixer.io/signup/free
    url = str.__add__('http://data.fixer.io/api/latest?access_key=', API_KEY)
    c = CurrencyConvertor(url)
    from_country = input("From Country: ")
    to_country = input("To Country: ")
    amount = int(input("Amount: "))
    
    c.convert(from_country, to_country, amount)
