from rest_framework import serializers
from primary_data import models


class CountrySerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Country
        fields = '__all__'


class StateSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.State
        fields = '__all__'


class CitySerializer(serializers.ModelSerializer):

    class Meta:
        model = models.City
        fields = '__all__'
