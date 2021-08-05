from django.core.management.base import BaseCommand
from currency.models import Currency
from datetime import datetime
import os
import csv


class Command(BaseCommand):
    help_text = 'Export currency data to csv file'

    def handle(self, *args, **options):
        try:
            cwd = os.getcwd()
            os.mkdir(os.path.join(cwd, 'csv_files'))

            print('Folder for csv files is created')
        except FileExistsError:
            print('Folder for csv files is already exists, skipped creating')

        filename = 'csv_files/currency_data_set_' + str(datetime.now())[:-7] + '.csv'
        with open(filename, mode='w') as csv_file:
            csv_writer = csv.writer(csv_file)
            HEADERS = ['NAME',
                       'SYMBOL',
                       'PRICE',
                       'CHANGE_30D',
                       'CHANGE_60D',
                       'CHANGE_90D',
                       'MAX_SUPPLY',
                       'CIRCULATING_SUPPLY']
            csv_writer.writerow(HEADERS)
            data_set = Currency.objects.all()
            for el in data_set:
                csv_writer.writerow([el.name,
                                     el.symbol,
                                     el.price,
                                     el.change_30d,
                                     el.change_60d,
                                     el.change_90d,
                                     el.max_supply,
                                     el.circulating_supply])

        print('Finished exporting data')
