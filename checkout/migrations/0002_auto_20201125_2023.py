# Generated by Django 3.1.2 on 2020-11-25 20:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='full_name',
            field=models.CharField(max_length=32),
        ),
    ]
