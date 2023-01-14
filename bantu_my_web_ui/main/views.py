from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
#request -> response
#a request handler

def greet(request):
    return render(request, 'mainpage.html')