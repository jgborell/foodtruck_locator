from rest_framework import generics, authentication
from models import *
from serializers import *
from django.conf import settings


class FoodTruckDetail(generics.RetrieveAPIView):
    serializer_class = FoodTruckSerializer
    queryset = FoodTruck.objects.all()


class FoodTruckList(generics.ListAPIView):
    serializer_class = FoodTruckSerializer
    queryset = FoodTruck.objects.all()


class AddFoodTruck(generics.CreateAPIView):
    serializer_class = FoodTruckSerializer


class FoodTruckStatus(generics.RetrieveUpdateAPIView):
    serializer_class = FoodTruckSerializer

    authentication_classes = (authentication.TokenAuthentication, )
    if settings.DEBUG:
        authentication_classes = (authentication.TokenAuthentication, authentication.SessionAuthentication)

    def get_object(self):
        return FoodTruck.objects.filter(owner=self.request.user)


class EditDeleteFoodTruck(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = FoodTruckSerializer

    authentication_classes = (authentication.TokenAuthentication, )
    if settings.DEBUG:
        authentication_classes = (authentication.TokenAuthentication, authentication.SessionAuthentication)

    def get_object(self):
        return FoodTruck.objects.filter(owner=self.request.user)


class MealDetail(generics.RetrieveAPIView):
    serializer_class = MealSerializer
    queryset = Meal.objects.all()


class MealList(generics.ListAPIView):
    serializer_class = MealSerializer
    queryset = Meal.objects.all()


class AddMeal(generics.CreateAPIView):
    serializer_class = MealSerializer

    authentication_classes = (authentication.TokenAuthentication, )
    if settings.DEBUG:
        authentication_classes = (authentication.TokenAuthentication, authentication.SessionAuthentication)

    def get_object(self):
        return Meal.objects.filter(owner=self.request.user)


class EditMeal(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = MealSerializer

    authentication_classes = (authentication.TokenAuthentication, )
    if settings.DEBUG:
        authentication_classes = (authentication.TokenAuthentication, authentication.SessionAuthentication)

    def get_object(self):
        return Meal.objects.filter(owner=self.request.user)
