import os

from django.conf import settings

from rate.models import Rate
from rate.tasks import parse_aval, parse_privatbank


class Response:
    pass


def test_privat(mocker):
    def mock():
        res = [
            {
                "ccy": "RUR",
                "base_ccy": "UAH",
                "buy": "0.28000",
                "sale": "0.32000"
            },
            {
                "ccy": "EUR",
                "base_ccy": "UAH",
                "buy": "19.20000",
                "sale": "20.00000"
            },
            {
                "ccy": "USD",
                "base_ccy": "UAH",
                "buy": "15.50000",
                "sale": "15.85000"
            }
        ]
        response = Response()
        response.json = lambda: res
        return response

    requests_get_patcher = mocker.patch('requests.get')
    requests_get_patcher.return_value = mock()
    rate_initial_count = Rate.objects.count()
    parse_privatbank()
    assert Rate.objects.count() == rate_initial_count + 4
    parse_privatbank()
    assert Rate.objects.count() == rate_initial_count + 4


def test_aval(mocker):
    def mock():
        path = os.path.join(settings.BASE_DIR, 'tests', 'html', 'aval.html')
        with open(path, encoding="WINDOWS-1251") as file:
            content = file.read()

        response = Response()
        response.status_code = 200
        response.text = content
        return response

    requests_get_patcher = mocker.patch('requests.get')
    requests_get_patcher.return_value = mock()
    parse_aval()
