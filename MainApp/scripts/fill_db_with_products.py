import os, django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'QASite.settings')
django.setup()

from MainApp.models import *
import random


def add_pcs(amount=30, category_name="Портативні комп'ютери", producers_names=('PC creator 3000', 'PC maker')):
    letters = 'ABCDEFGHKJ'
    category = Category.objects.get(name=category_name)
    producers = [Producer.objects.get(name=name) for name in producers_names]

    names = []
    for i in range(amount):
        while True:
            name = f'Gen computer {random.choice(letters)}{random.randint(10, 99)}'
            if name in names:
                continue

            Product.objects.create(
                name=name,
                producer=random.choice(producers),
                category=category,
                price=100 * random.randint(200, 1500)
            )
            names.append(name)
            break


if __name__ == '__main__':
    add_pcs()
