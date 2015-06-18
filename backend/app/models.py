from django.db import models
from django.contrib.auth.models import User


class FoodTruck(models.Model):

    STATUS_CHOICES = (
        (1, 'Off-Duty'),
        (2, 'In-Route'),
        (3, 'Taking Orders')
    )

    name = models.CharField(max_length=30)
    username = models.CharField(max_length=20)
    twitter_handle = models.CharField(max_length=30)
    twitter_id = models.IntegerField()
    email = models.EmailField('email address', max_length=100, unique=True)
    website = models.CharField(max_length=50, null=True, blank=True)
    phone_number = models.IntegerField(null=True, blank=True)
    latitude = models.DecimalField(max_digits=17, decimal_places=14, default=0.0, null=True, blank=True)
    longitude = models.DecimalField(max_digits=17, decimal_places=14, default=0.0, null=True, blank=True)
    status = models.IntegerField(choices=STATUS_CHOICES, default=1)
    owner = models.ForeignKey(User, related_name="owner")

    def __unicode__(self):
        return self.name


class Meal(models.Model):
    name = models.CharField(max_length=30)
    truck = models.ForeignKey(FoodTruck, related_name="truck")
    description = models.TextField()
    allergies = models.ManyToManyField(Allergies)

    def __unicode__(self):
        return self.name


class Allergies(models.Model):
    name = models.CharField(max_length=30)

    def __unicode__(self):
        return self.name
