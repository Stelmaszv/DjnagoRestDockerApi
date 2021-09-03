from django.urls import path
from apps.cars.views import CarList,CarListPupular
app_name = 'cars'

urlpatterns = [
    path('cars',    CarList.as_view()        ,name='cars_list'),
    path('popular', CarListPupular.as_view() ,name='cars_popular'),
]