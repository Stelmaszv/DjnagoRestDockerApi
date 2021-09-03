from django.urls import path
from apps.cars.views import CarList,CarListPupular,AddRate,CarDelete
app_name = 'cars'

urlpatterns = [
    path('rate',    AddRate.as_view(),name='add_rate'),
    path('cars',    CarList.as_view()        ,name='cars_list'),
    path('popular', CarListPupular.as_view() ,name='cars_popular'),
    path('cars/<int:id>/',CarDelete.as_view(), name="car_delete")
]