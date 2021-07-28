from django.core.management.base import BaseCommand
from requests import Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
from weather_app.settings import CRYPTOCURRENCY_ACCESS_KEY
from currency.models import CurrencyData, Currency
import json


class Command(BaseCommand):
    help_text = 'Parse data from CryptoData'

    def handle(self, *args, **options):
        print('Initialized parsing data')
        for curr_data in CurrencyData.objects.filter(status=1).all():
            name = curr_data.name
            symbol = curr_data.data['symbol']
            price = curr_data.data['quote']['USD']['price']
            change_30d = curr_data.data['quote']['USD']['percent_change_30d']
            change_60d = curr_data.data['quote']['USD']['percent_change_60d']
            change_90d = curr_data.data['quote']['USD']['percent_change_90d']
            max_supply = curr_data.data['max_supply']
            circulating_supply = curr_data.data['circulating_supply']
            print(f'{name=},'
                  f'{symbol=},'
                  f'{price=},'
                  f'{change_30d=},'
                  f'{change_60d=},'
                  f'{change_90d=},'
                  f'{max_supply=},'
                  f'{circulating_supply=}')
            Currency.objects.get_or_create(name=name,
                                           symbol=symbol,
                                           price=price,
                                           change_30d=change_30d,
                                           change_60d=change_60d,
                                           change_90d=change_90d,
                                           max_supply=max_supply,
                                           circulating_supply=circulating_supply)
            curr_data.status = 2
            curr_data.save()
        print('Finished processing data')
