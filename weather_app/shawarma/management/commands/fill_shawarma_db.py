from urllib.request import urlopen
from bs4 import BeautifulSoup
from django.core.management.base import BaseCommand
from shawarma.models import Shawarma, Ingredient


class Command(BaseCommand):
    help_text = 'fill db for Category and Goods'

    def handle(self, *args, **options):
        base_url = r'https://shaurman.com.ua/shaurma'

        item_class = {'class': 'product-layout products__item'}
        item_link = {'class': 'products__item-title'}
        item_price = {'class': 'products__item-price'}
        item_weight = {'class': 'products__item-weight'}
        item_ingredients_container = {'class': 'product-ingridients product-ingridients--checked'}
        item_ingredients_text = {'class': 'product-ingridients__ingridient-title'}

        client = urlopen(base_url)
        page = client.read()
        client.close()
        page_souped = BeautifulSoup(page, 'html.parser')
        items = page_souped.findAll('div', item_class)

        for item in items:
            name = item.find('a', item_link).text.strip().replace('+', ' ')
            price = item.find('p', item_price).text.strip().replace(' грн', '')
            weight = item.find('p', item_weight).text.strip().replace(' г.', '')
            local_url = item.find('a', item_link)['href']

            local_client = urlopen(local_url)
            local_page = local_client.read()
            local_client.close()
            local_page_souped = BeautifulSoup(local_page, 'html.parser')
            local_ingredients = local_page_souped.find('ul', item_ingredients_container).findAll('p', item_ingredients_text)
            ingredients = [item.text.strip() for item in local_ingredients if ' грн' not in item.text]

            print(f'{name=}',
                  f'{price=}',
                  f'{weight=}',
                  # f'{local_url=}',
                  f'{ingredients=}')

            ingredients_to_set = []
            for el in ingredients:
                ingredient = Ingredient.objects.get_or_create(name=el)
                ingredients_to_set.append(ingredient[0])

            shawarma = Shawarma.objects.create(name=name, price=price, weight=weight)
            shawarma.ingredients.set(ingredients_to_set)