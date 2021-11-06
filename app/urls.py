from django.urls import path
from django.views.generic import TemplateView

from . import views

urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    path('about-us', views.AboutUsView, name='about_us'),
    path('contact-us', views.ContactUsView, name='contact_us'),
    path('faq', views.FaqView, name='faq'),
    path('privacy-policy', views.PrivacyPolicyView, name='privacy_policy'),
    path('terms-and-condition', views.TermsAndConditionView,
         name='termas_and_condition'),

]
