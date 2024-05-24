from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
def fun1(request):
    return HttpResponse("Hello, World!")

# Static html
# from django.template import loader
# def fun2(request):
#     return HttpResponse(loader.get_template('first.html').render())

# Dynamic html
from .models import Demo1
from django.template import loader
def fun3(request):
    form1 = {'fname':'','lname':''}
    if request.method == "POST":
        form1['fname'] = request.POST.get('fname')
        form1['lname'] = request.POST.get('lname')
        # d1 = Demo1()
        # d1.firstname = form1['fname']
        # d1.lastname = form1['lname']
        # d1.save()
    return HttpResponse(loader.get_template('first.html').render(form1, request))