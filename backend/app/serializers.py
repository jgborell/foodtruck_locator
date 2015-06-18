from rest_framework import serializers
from app.models import FoodTruck, Meal


class FoodTruckSerializer(serializers.ModelSerializer):
    class Meta:
        model = FoodTruck


class MealSerializer(serializers.ModelSerializer):
    class Meta:
        model = Meal
