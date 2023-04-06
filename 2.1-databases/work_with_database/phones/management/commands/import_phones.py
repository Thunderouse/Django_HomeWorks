import csv

from django.core.management.base import BaseCommand
from datetime import datetime
from phones.models import Phone


class Command(BaseCommand):
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        with open('phones.csv', 'r', encoding='utf-8') as file:
            phones = list(csv.DictReader(file, delimiter=';'))

        for phone in phones:
            Phone(
                id = phone['id'],
                name = phone['name'],
                image = phone['image'],
                price = phone['price'],
                release_date = datetime.toordinal(datetime.strptime(phone['release_date'], "%Y-%m-%d")),
                lte_exists = phone['lte_exists'],).save()

