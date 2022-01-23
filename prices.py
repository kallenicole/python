#Welcome to Alpha Vantage! Here is your API key: 079QA5TY8XF0VDBT

import json
import requests
import sys

def main():
    stock_symbol = sys.argv[1]
    url = 'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=&apikey=079QA5TY8XF0VDBT'
    params = {'symbol': stock_symbol, 'outputsize': 'full'}
    response = requests.get(url, params=params)
    usable_response = json.loads(response.text)
    
    #pass in the usable json text
    date_results = unpack_dates(usable_response)
    price_results = unpack_prices(usable_response)
    #change stock prices from str to float
    num_price_results = [float(num) for num in price_results]

    #iterate through lists and format 
    passing_this_to_file = ''
    for i in range(len(date_results)):
        passing_this_to_file += ("{} ${:>.2f}\n").format(date_results[i], num_price_results[i])
    
    #write to a file with stock symbol
    with open("prices." + stock_symbol + ".txt", "w") as fd:
        fd.write(passing_this_to_file)
    print("Wrote historical price data for MSFT to file prices.MSFT.txt")

#make a list of the dates from json data
def unpack_dates(stock_price_dict):
    date_lst = []
    for dates in stock_price_dict['Time Series (Daily)']:
        date_lst.append(dates)
    return date_lst

#make a list of prices from json data
def unpack_prices(stock_price_dict):
    price_lst = []
    for stock_prices in stock_price_dict['Time Series (Daily)']:
        prices = stock_price_dict['Time Series (Daily)'][stock_prices]['4. close']
        price_lst.append(prices)
    return price_lst

main()


