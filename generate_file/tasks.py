import csv

from django.db import transaction
from faker import Faker
from celery import shared_task
from .models import FileCSVModel
from django.core.files import File
import os

fake = Faker()


@shared_task
def generate_file(filename, data_count):
    with open('media/temp.csv', mode='w') as file:
        file_writer = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        file_writer.writerow(['first_name', 'last_name', 'age'])
        for _ in range(data_count):
            file_writer.writerow([fake.first_name(), fake.last_name(), fake.numerify("@#")])







