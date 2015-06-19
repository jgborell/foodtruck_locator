# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Allergies',
            new_name='Allergy',
        ),
        migrations.AlterModelOptions(
            name='allergy',
            options={'verbose_name_plural': 'Allergies'},
        ),
    ]
