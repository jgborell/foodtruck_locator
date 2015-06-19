# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20150619_1815'),
    ]

    operations = [
        migrations.AlterField(
            model_name='foodtruck',
            name='owner',
            field=models.ForeignKey(related_name='truck', to=settings.AUTH_USER_MODEL),
        ),
    ]
