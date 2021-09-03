from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import  APIView
class APIPrototypeGet(APIView):
    serializer_class=None
    queryset=None

    def get(self, request, *args, **kwargs):
        return self.api_get(request)

    def api_get(self, request, *args, **kwargs):
        serializer = self.serializer_class(self.queryset)
        return Response(data=serializer.data, status=status.HTTP_200_OK)