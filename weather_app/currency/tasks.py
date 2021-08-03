from celery import shared_task
from .models import Currency, CurrencyAverage
from random import randint
from statistics import mean


@shared_task
def process_average():
    print('Starting task \"process_average\"')

    currency_count = Currency.objects.count() - 1
    obj = Currency.objects.get(id=randint(0, currency_count))
    print(f'Processing {obj}')

    avg_value = mean([obj.change_30d, obj.change_60d, obj.change_90d])
    print(f'Got value {avg_value}')

    CurrencyAverage.objects.get_or_create(name=obj.name, avg_value=avg_value)
    print('End of \"process_average\" task')
