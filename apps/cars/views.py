from django.http import Http404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import  APIView
from .models import Car,Rate
from .serializers import CarSerializer,CarSerializerPopular,RateSerializer,CarDeleteSerializer
class APIPrototypeGet(APIView):
    SerializerClass=None
    queryset=None

    def get(self, request, *args, **kwargs):
        return self.api_get(request)

    def api_get(self, request, *args, **kwargs):
        serializer = self.SerializerClass(self.queryset)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

class APIPrototype(APIView):

    SerializerClass = None
    many     = True
    queryset = ''
    order_by = ''

    def list(self):
        serializer = self.SerializerClass(self.queryset, many=self.many)
        if len(self.order_by):
            list = sorted(
                serializer.data,
                key=lambda tup: tup[self.order_by],
                reverse=True)
        else:
            list= serializer.data
        return list

    def post(self, request, *args, **kwargs):
        serializer = self.SerializerClass(data=request.data, many=False)
        if serializer.is_valid():
            serializer.save()
            return Response(data=self.list(), status=status.HTTP_201_CREATED)
        return self.api_get(request)

    def api_get(self, request, *args, **kwargs):
        return Response(data=self.list(), status=status.HTTP_200_OK)

    def get(self, request, *args, **kwargs):
        return self.api_get(request)

class CarDelete(APIPrototypeGet):

    many             = False
    SerializerClass = CarDeleteSerializer
    queryset = Car.objects

    def get_object(self, pk):
        try:
            return Car.objects.get(pk=pk)
        except Car.DoesNotExist:
            raise Http404

    def delete(self, request, *args, **kwargs):
        car = self.get_object(self.kwargs.get("id"))
        car.delete()
        mess =str(car)+' Has been removed from data base'
        return Response(data=mess, status=status.HTTP_200_OK)

class CarList (APIPrototype):
    SerializerClass  = CarSerializer
    queryset          = Car.objects
    order_by          = 'avg_rating'

class CarListPupular (APIPrototype):
    SerializerClass = CarSerializerPopular
    queryset         = Car.objects
    order_by         = 'rates_number'

class AddRate(APIPrototype):
    SerializerClass = RateSerializer
    queryset=  Rate.objects