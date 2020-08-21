from time import sleep
import random
from fake_useragent import UserAgent

import requests
from bs4 import BeautifulSoup


def random_sleep():
    sleep(random.randint(1, 3))


BASE_URL = 'https://www.work.ua/ru/jobs/'
ua = UserAgent()

# response = requests.get(BASE_URL + '?page=1')  WRONG
with open('workua.txt', 'w') as file:
    page = 0

    while True:
        page += 1
        print(f'start to parse page: {page}')

        headers = {'User-Agent': ua.random}

        response = requests.get(BASE_URL, params={'page': page}, headers=headers)
        response.raise_for_status()
        # random_sleep()

        soup = BeautifulSoup(response.text, 'html.parser')

        res = soup.find('div', {'id': 'pjax-job-list'})

        if res is None:
            break

        res = res.find_all('h2')
        for elem in res:
            href = elem.find('a').attrs['href']
            file.write(f'{href}\n')
