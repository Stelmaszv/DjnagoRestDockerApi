from django.test import TestCase
from rest_framework.test import APITestCase
from django.urls import resolve
from django.urls import reverse
from rest_framework import status
from .models import Car,Rate
import json
from django.test import Client
from .views import CarList,AddRate,CarListPupular,CarDelete
from .serializers import CarSerializer
#dqd
class AbstratTest(APITestCase):
    many=True

    def data_match(self):
        response = self.client.get(self.url_test)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def view_match(self,view):
        self.assertEquals(resolve(self.url_test).func.view_class, view)

class CarDelete_test(AbstratTest):
    url_test_delete = reverse("car_delete", kwargs={"id":0})

    def setUp(self):
        self.client = Client()
        data = Car.objects.create(make="BUICK", model="BUICK")

    def test_data_match_and_view_match(self):
        self.data_match()
        self.view_match(CarDelete)
    def test_delete_car(self):
        self.assertEqual(Car.objects.count(), 1)
        response = self.client.delete(self.url_test_delete)
        self.assertEqual(Car.objects.count(),0)

class CarList_test(AbstratTest):
    url_test = reverse("cars_list", kwargs={})
    url_test_delete = reverse("car_delete", kwargs={"id":0})

    def setUp(self):
        self.client = Client()

    def test_data_match_and_view_match(self):
        self.data_match()
        self.view_match(CarList)
    def test_add_car(self):
        data_post= {
            "make": "BUICK",
            "model": "nice"
        }
        self.assertEqual(Car.objects.count(), 0)
        response = self.client.post(self.url_test, data_post)
        self.assertEqual(Car.objects.count(), 1)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

class CarPopular_test(AbstratTest):

    url_test = reverse("cars_popular", kwargs={})

    def test_data_match_and_view_match(self):
        self.data_match()
        self.view_match(CarListPupular)

class Rate_test(AbstratTest):
    url_test = reverse("add_rate", kwargs={})

    def setUp(self):
        self.client = Client()

    def test_data_match_and_view_match(self):
        self.data_match()
        self.view_match(AddRate)

    def test_add_car(self):
        car = Car.objects.create(make="BUICK", model="BUICK")
        data = Rate.objects.create(rating=5, car_id=car)
        data_post= {
            "car_id": 1,
            "rating": 5
        }
        response = self.client.post(self.url_test, data_post)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
