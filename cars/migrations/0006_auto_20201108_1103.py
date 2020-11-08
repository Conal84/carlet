# Generated by Django 3.1.2 on 2020-11-08 11:03

import datetime
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0005_auto_20201107_1841'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='car',
            name='insurance',
        ),
        migrations.RemoveField(
            model_name='car',
            name='num_days',
        ),
        migrations.RemoveField(
            model_name='car',
            name='support',
        ),
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('hired_from', models.DateField(default=datetime.date.today)),
                ('hired_to', models.DateField(default=datetime.date.today)),
                ('num_days', models.IntegerField(default=0)),
                ('insurance', models.DecimalField(decimal_places=0, default=0, max_digits=3)),
                ('support', models.DecimalField(decimal_places=0, default=0, max_digits=3)),
                ('car', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cars.car')),
            ],
        ),
    ]