from django.urls import path
from apps.cars.views import CarList
app_name = 'cars'

urlpatterns = [
    path('carslist', CarList.as_view(),name='cars_list'),
]