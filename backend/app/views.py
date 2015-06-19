from rest_framework import generics, authentication
from models import *
from serializers import *
from django.conf import settings


class FoodTruckDetail(generics.RetrieveAPIView):
    serializer_class = FoodTruckSerializer
    queryset = FoodTruck.objects.all()
    lookup_url_kwarg = 'ft_pk'


class FoodTruckList(generics.ListAPIView):
    serializer_class = FoodTruckSerializer

    # if guest user wants to view the food  truck list, they will get all food trucks available,
    # if a registered food truck owner views the food truck list, they will only get their food truck(s)
    def get_queryset(self):
        # if self.request.user:
        #     return FoodTruck.objects.filter(owner=self.request.user)
        return FoodTruck.objects.all()


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
    lookup_url_kwarg = 'meal_pk'


class MealList(generics.ListAPIView):
    serializer_class = MealSerializer
    lookup_url_kwarg = 'ft_pk'

    def get_queryset(self):
        return Meal.objects.filter(truck=self.kwargs['ft_pk'])


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
