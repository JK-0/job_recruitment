from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register('country', views.CountryViewSet, basename='country')
router.register('state', views.StateViewSet, basename='state')
router.register('city', views.CityViewSet, basename='city')


urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls')),

]
