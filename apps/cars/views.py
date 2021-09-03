from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import  APIView
from .models import Car
from .serializers import CarSerializer,CarSerializerPopular
class APIPrototypeGet(APIView):
    serializer_class=None
    queryset=None

    def get(self, request, *args, **kwargs):
        return self.api_get(request)

    def api_get(self, request, *args, **kwargs):
        serializer = self.serializer_class(self.queryset)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

class APIPrototype(APIView):

    serializer_class = None
    many     = True
    queryset = ''
    order_by = ''

    def list(self):
        serializer = self.serializer_class(self.queryset, many=self.many)
        if len(self.order_by):
            list = sorted(serializer.data, key=lambda tup: tup[self.order_by],reverse=True)
        else:
            list= serializer.data
        return list

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,many=False)
        if serializer.is_valid():
            serializer.save()
            return Response(data=self.list(), status=status.HTTP_201_CREATED)
        return self.api_get(request)

    def api_get(self, request, *args, **kwargs):
        return Response(data=self.list(), status=status.HTTP_200_OK)

    def get(self, request, *args, **kwargs):
        return self.api_get(request)

class CarList (APIPrototype):
    serializer_class  = CarSerializer
    queryset          = Car.objects
    order_by          = 'avg_rating'

class CarListPupular (APIPrototype):
    serializer_class = CarSerializerPopular
    queryset         = Car.objects
    order_by         = 'rates_number'