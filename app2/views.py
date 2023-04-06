from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def first_app2(request):
    return HttpResponse('<h1><marquee>This is app2 first function</marquee></h1>')

def second_app2(request):
    return HttpResponse('<h1><marquee>This is app2 second function</marquee></h1>')
