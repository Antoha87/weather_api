from django.core.management.base import BaseCommand
from requests import Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
from weather_app.settings import CRYPTOCURRENCY_ACCESS_KEY
from currency.models import CurrencyData
import json


class Command(BaseCommand):
    help_text = 'Fill db for Cryptocurrencies'

    def handle(self, *args, **options):
        print("Initiated fill_db")

        url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
        parameters = {
            'start': '1',
            'limit': '50',
            'convert': 'USD'
        }
        headers = {
            'Accepts': 'application/json',
            'X-CMC_PRO_API_KEY': CRYPTOCURRENCY_ACCESS_KEY,
        }

        session = Session()
        session.headers.update(headers)

        try:
            response = session.get(url, params=parameters)
            data = json.loads(response.text)
            # print(data)
            for item in data['data']:
                name = item['name']
                created = item['date_added']
                print(f'{name=}, {created=}')
                currency = CurrencyData.objects.get_or_create(name=name,
                                                              created=created,
                                                              data=item)

        except (ConnectionError, Timeout, TooManyRedirects) as e:
            print(e)

        print("Finished filling db")
