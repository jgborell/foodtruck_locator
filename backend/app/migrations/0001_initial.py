# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Allergies',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='FoodTruck',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=30)),
                ('username', models.CharField(max_length=20)),
                ('twitter_handle', models.CharField(max_length=30)),
                ('twitter_id', models.IntegerField()),
                ('email', models.EmailField(unique=True, max_length=100, verbose_name=b'email address')),
                ('website', models.CharField(max_length=50, null=True, blank=True)),
                ('phone_number', models.IntegerField(null=True, blank=True)),
                ('latitude', models.DecimalField(default=0.0, null=True, max_digits=17, decimal_places=14, blank=True)),
                ('longitude', models.DecimalField(default=0.0, null=True, max_digits=17, decimal_places=14, blank=True)),
                ('status', models.IntegerField(default=1, choices=[(1, b'Off-Duty'), (2, b'In-Route'), (3, b'Taking Orders')])),
                ('owner', models.ForeignKey(related_name='owner', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Meal',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=30)),
                ('description', models.TextField()),
                ('allergies', models.ManyToManyField(to='app.Allergies')),
                ('truck', models.ForeignKey(related_name='truck', to='app.FoodTruck')),
            ],
        ),
    ]
