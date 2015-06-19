# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20150618_1821'),
    ]

    operations = [
        migrations.AlterField(
            model_name='foodtruck',
            name='email',
            field=models.EmailField(max_length=100, verbose_name=b'email address'),
        ),
        migrations.AlterField(
            model_name='foodtruck',
            name='twitter_handle',
            field=models.CharField(unique=True, max_length=30),
        ),
        migrations.AlterField(
            model_name='foodtruck',
            name='twitter_id',
            field=models.IntegerField(unique=True),
        ),
    ]
