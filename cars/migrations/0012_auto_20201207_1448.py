# Generated by Django 3.1.2 on 2020-12-07 14:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('cars', '0011_remove_car_num_days'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='car',
            name='account',
        ),
        migrations.AddField(
            model_name='car',
            name='user',
            field=models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
