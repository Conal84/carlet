# Generated by Django 3.1.2 on 2020-12-06 15:01

from django.db import migrations
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0004_auto_20201206_1340'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='default_country',
            field=django_countries.fields.CountryField(default=' ', max_length=2),
            preserve_default=False,
        ),
    ]
