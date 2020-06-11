from celery import shared_task

from rate import model_choices as mch
from rate.utils import to_decimal

import requests
from bs4 import BeautifulSoup


@shared_task
def parse_privatbank():
    from rate.models import Rate

    url = "https://api.privatbank.ua/p24api/pubinfo?json&exchange&coursid=5"
    response = requests.get(url)
    currency_type_mapper = {
        'USD': mch.CURRENCY_TYPE_USD,
        'EUR': mch.CURRENCY_TYPE_EUR,
    }
    for item in response.json():

        if item['ccy'] not in currency_type_mapper:
            continue

        currency_type = currency_type_mapper[item['ccy']]

        # buy
        amount = to_decimal(item['buy'])

        last = Rate.objects.filter(
            source=mch.SOURCE_PRIVATBANK,
            currency_type=currency_type,
            type=mch.RATE_TYPE_BUY,
        ).last()

        if last is None or last.amount != amount:
            Rate.objects.create(
                amount=amount,
                source=mch.SOURCE_PRIVATBANK,
                currency_type=currency_type,
                type=mch.RATE_TYPE_BUY,
            )

        # sale
        amount = to_decimal(item['sale'])

        last = Rate.objects.filter(
            source=mch.SOURCE_PRIVATBANK,
            currency_type=currency_type,
            type=mch.RATE_TYPE_SALE,
        ).last()

        if last is None or last.amount != amount:
            Rate.objects.create(
                amount=amount,
                source=mch.SOURCE_PRIVATBANK,
                currency_type=currency_type,
                type=mch.RATE_TYPE_SALE,
            )


@shared_task
def parse_monobank():
    pass


@shared_task
def parse_aval():
    from rate.models import Rate

    url = 'https://ex.aval.ua/ru/personal/everyday/exchange/exchange/'

    response = requests.get(url)
    assert response.status_code == 200

    soup = BeautifulSoup(response.text, 'html.parser')
    mydivs = soup.findAll("div", {"class": "body-currency"})
    rates = mydivs[0].findAll('td', {'class': 'right'})

    rates = [to_decimal(rate.text.replace(',', '.')) for rate in rates]
    rates_to_save = [
        {'amount': rates[0], 'currency_type': mch.CURRENCY_TYPE_USD, 'type': mch.RATE_TYPE_SALE},
        {'amount': rates[1], 'currency_type': mch.CURRENCY_TYPE_USD, 'type': mch.RATE_TYPE_BUY},
        {'amount': rates[2], 'currency_type': mch.CURRENCY_TYPE_EUR, 'type': mch.RATE_TYPE_SALE},
        {'amount': rates[3], 'currency_type': mch.CURRENCY_TYPE_EUR, 'type': mch.RATE_TYPE_BUY},
    ]

    for rate in rates_to_save:
        amount = rate['amount']
        last = Rate.objects.filter(
            source=mch.SOURCE_AVAL,
            currency_type=rate['currency_type'],
            type=rate['type'],
        ).last()

        if last is None or last.amount != amount:
            Rate.objects.create(
                amount=amount,
                source=mch.SOURCE_AVAL,
                currency_type=rate['currency_type'],
                type=rate['type'],
            )


@shared_task
def parse():
    parse_monobank.delay()
    parse_privatbank.delay()
    parse_aval.delay()
