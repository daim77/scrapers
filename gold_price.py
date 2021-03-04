# ===== gold price scraping from business insider =====
import csv
from datetime import datetime
import requests
import bs4


URL = 'https://markets.businessinsider.com/commodities/gold-price'


def write_price_to_csv(price):
    with open('/Users/martindanek/Documents/programovani/files/csv/gold.csv', 'a') as file:
        writer = csv.writer(file)
        writer.writerow([price, datetime.now().strftime('%d %b %Y %H %M')])


def get_gold_price():
    price = 'price not found'
    request_data = requests.get(URL)
    soup = bs4.BeautifulSoup(request_data.text, "html.parser")

    data = soup.find('div', class_="snapshot").script.string
    data_list = [item.strip(',:') for item in data.split()]
    for i, item in enumerate(data_list):
        if item == 'price':
            price = data_list[i + 1]
            break
    write_price_to_csv(price)


if __name__ == '__main__':
    get_gold_price()
