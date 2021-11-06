from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework import filters
from rest_framework import permissions
from primary_data import serializers
from primary_data import models


class CountryViewSet(viewsets.ModelViewSet):
    """Handle creating, creating and updating Country"""
    serializer_class = serializers.CountrySerializer
    queryset = models.Country.objects.all()
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name',)
    permission_classes = [permissions.IsAuthenticated]


class StateViewSet(viewsets.ModelViewSet):
    """Handle creating, creating and updating State"""
    serializer_class = serializers.StateSerializer
    queryset = models.State.objects.all()
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name',)


class CityViewSet(viewsets.ModelViewSet):
    """Handle creating, creating and updating Chapter"""
    serializer_class = serializers.CitySerializer
    queryset = models.City.objects.all()
