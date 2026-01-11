from django.shortcuts import render
from houses.models import House



def home(request):
    houses = House.objects.all()[:6]
    return render(request, 'home.html', {'houses': houses})


def about(request):
    return render(request, 'about.html', {})


def contact_us(request):
    return render(request, 'contact_us.html', {})