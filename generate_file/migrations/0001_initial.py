# Generated by Django 4.1.2 on 2022-10-13 05:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FileCSVModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('filename', models.CharField(max_length=254)),
                ('file', models.FileField(max_length=254, upload_to='data/')),
            ],
        ),
    ]