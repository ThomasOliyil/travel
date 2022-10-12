from django.http import HttpResponse
from django.shortcuts import render
from .models import place
from .models import adm

def demo(request):
    obj = place.objects.all()
    obj1 = adm.objects.all()
    return render(request,"index.html", {'result': obj,'result1': obj1})