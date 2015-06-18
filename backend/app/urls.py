from django.conf.urls import url
from views import *

urlpatterns = [
    url(r'^food-truck/$', FoodTruckList.as_view(), name='food-truck-list'),
    url(r'^food-truck/(?P<pk>[0-9]+)/$', FoodTruckDetail.as_view(), name='food-truck-detail'),
    url(r'^edit-food-truck/(?P<pk>[0-9]+)/$', EditDeleteFoodTruck.as_view(), name='edit-food-truck'),
    url(r'^add-food-truck/$', AddFoodTruck.as_view(), name='add-food-truck'),
    url(r'^update-status/(?P<pk>[0-9]+)/$', FoodTruckStatus.as_view(), name='update-status'),
    url(r'^food-truck/$', FoodTruckList.as_view(), name='food-truck-list'),
    url(r'^food-truck/(?P<pk>[0-9]+)/$', FoodTruckDetail.as_view(), name='food-truck-detail'),
]
