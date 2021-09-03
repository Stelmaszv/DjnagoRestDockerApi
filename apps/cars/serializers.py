from rest_framework import serializers
from .models import Car,Rate

class CarDeleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = ['id']

class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = ['id', 'make','model','avg_rating']

class CarSerializerPopular(serializers.ModelSerializer):

    class Meta:
        model = Car
        fields = ['id', 'make','model','rates_number']

class RateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Rate
        fields = ['id','rating','car_id']