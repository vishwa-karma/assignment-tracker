# Generated by Django 3.0.3 on 2020-04-09 01:56

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0002_create_initial_grades'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assignment',
            name='duedate',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now),
        ),
    ]
