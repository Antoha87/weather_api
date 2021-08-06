from django.core.management.base import BaseCommand
from currency.models import User
from faker import Faker


class Command(BaseCommand):
    help_text = 'Fill db for Users'

    def handle(self, *args, **options):
        print("Initiated fill_db")

        faker = Faker()

        for _ in range(100):
            User.objects.create(name=faker.name(),
                                email=faker.email())

        print("Finished filling db")
