from relations.models import Category, Goods
from django.core.management.base import BaseCommand
import random
from faker import Faker


class Command(BaseCommand):
    help_text = 'fill db for Category and Goods'

    def handle(self, *args, **options):
        print("Initiated fill_db")

        fake = Faker()

        for _ in range(random.randint(5, 10)):
            cat_name = fake.text(max_nb_chars=random.randint(8, 40))
            cat = Category.objects.create(name=cat_name, slug=fake.slug(cat_name))

            for _ in range(random.randint(5, 10)):
                Goods.objects.create(name=fake.name(), category=cat, price=random.randint(1, 100))

        print("Finished filling db")