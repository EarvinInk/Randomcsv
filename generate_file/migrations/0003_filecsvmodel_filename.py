# Generated by Django 4.1.2 on 2022-10-13 10:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('generate_file', '0002_remove_filecsvmodel_filename'),
    ]

    operations = [
        migrations.AddField(
            model_name='filecsvmodel',
            name='filename',
            field=models.CharField(default=0, max_length=254),
            preserve_default=False,
        ),
    ]
