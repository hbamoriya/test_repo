# Generated by Django 3.2.4 on 2021-07-23 10:49

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('Newbie', '0006_remove_allcourses_startedfrom'),
    ]

    operations = [
        migrations.AddField(
            model_name='allcourses',
            name='startedfrom',
            field=models.DateTimeField(default=datetime.datetime(2021, 7, 23, 10, 49, 42, 539447, tzinfo=utc), verbose_name='started From'),
            preserve_default=False,
        ),
    ]
