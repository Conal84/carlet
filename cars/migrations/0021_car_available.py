# Generated by Django 3.1.2 on 2021-01-08 18:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0020_remove_car_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='available',
            field=models.BooleanField(default=True),
        ),
    ]
