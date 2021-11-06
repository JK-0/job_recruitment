from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.


class HomePageView(TemplateView):
    template_name = 'home.html'


def AboutUsView(request):
    context = {}
    return render(request, 'about_us.html', context)


def ContactUsView(request):
    context = {}
    return render(request, 'contact_us.html', context)


def FaqView(request):
    context = {}
    return render(request, 'faq.html', context)


def PrivacyPolicyView(request):
    context = {}
    return render(request, 'privacy_policy.html', context)


def TermsAndConditionView(request):
    context = {}
    return render(request, 'terms_and_condition.html', context)
