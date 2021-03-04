# ===== FIO transparent account scrapper =====

import requests
import csv
import bs4


def compose_url(account, date_from, date_to):
    return 'https://ib.fio.cz/ib/transparent?a='\
           + str(account) + '&f='\
           + str(date_from)\
           + '&t='\
           + str(date_to)


def write_data(arg, account):
    with open(f'/Users/martindanek/Documents/programovani/files/csv/fio_'
              f'{str(account)}.csv', 'w') as file:
        writer = csv.writer(file)
        writer.writerows(arg)


def fio_account(account, date_from, date_to):

    url = compose_url(account, date_from, date_to)
    data = requests.get(url)

    soup = bs4.BeautifulSoup(data.text, 'html.parser')

    header = [
        item.text
        for item in
        soup.find('table').find_next('table').find('thead').find_all('th')
    ]

    transaction = [
        item
        for item in
        soup.find('table').find_next('table').find('tbody').find_all('td')
    ]

    clean_data = []
    sub_list = []
    clean_data.append(header)

    for index, item in enumerate(transaction):
        sub_list.append(item.text.strip('\n \t'))
        if (index + 1) % 9 == 0:
            clean_data.append(sub_list)
            sub_list = []
    write_data(clean_data, account)


if __name__ == '__main__':
    fio_account(2801343758, '01.01.2021', '29.01.2021')
