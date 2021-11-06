"""job_recruitment URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from .views import *

urlpatterns = [
    path('key-skill-autocomplete', KeySkillAutocomplete.as_view(create_field='skill'),
         name='key-skill-autocomplete',),
    path('university-autocomplete', UniversityAutocomplete.as_view(create_field='name'),
         name='university-autocomplete',),
    path('course-name-autocomplete', CourseNameAutocomplete.as_view(),
         name='course-name-autocomplete',),
    path('specialization-autocomplete', SpecializationAutocomplete.as_view(),
         name='specialization-autocomplete',),
    path('role-autocomplete', RoleAutocomplete.as_view(),
         name='role-autocomplete',),
    path('designation-autocomplete', DesignationAutocomplete.as_view(),
         name='designation-autocomplete',),
    path('state-autocomplete', StateAutocomplete.as_view(),
         name='state-autocomplete',),
    path('city-autocomplete', CityAutocomplete.as_view(),
         name='city-autocomplete',),

]
