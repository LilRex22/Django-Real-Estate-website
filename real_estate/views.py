from django.shortcuts import render
from houses.models import House



def home(request):
    houses = House.objects.all()[:6]
    return render(request, 'home.html', {'houses': houses})