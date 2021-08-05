from celery import shared_task
from .models import Currency, CurrencyAverage
from weather_app.celery import app as celery_app
from random import randint
from statistics import mean
from functools import wraps


def task_dec(func):
    @wraps(func)
    def wrapper():
        print(f'Starting task "{func.__name__}"')
        return func()
    return wrapper


@shared_task
@task_dec
def process_average():
    currency_count = Currency.objects.count() - 1
    try:
        obj = Currency.objects.get(id=randint(0, currency_count))
    except ValueError:
        print('Failed getting a "Currency" object, skipping... Database is probably empty!')
    else:
        print(f'Processing {obj}')

        avg_value = mean([obj.change_30d, obj.change_60d, obj.change_90d])
        print(f'Got value {avg_value}')

        CurrencyAverage.objects.get_or_create(name=obj.name, avg_value=avg_value)


@celery_app.task(name="get sum of currencies")
@task_dec
def sum_of_currencies():
    currency_count = Currency.objects.count() - 1

    try:
        obj = Currency.objects.get(id=randint(0, currency_count))
    except ValueError:
        print('Failed getting a "Currency" object, skipping... Database is probably empty!')
    else:
        print(f'Processing {obj}')

        sum_value = sum([obj.change_30d, obj.change_60d, obj.change_90d])
        print(f'Got value {sum_value}')
