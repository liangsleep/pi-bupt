from django.shortcuts import render
from django.http import HttpResponse

def home_page(requset):
    return HttpResponse('<html><title>To-Do lists</title></html>')
    pass

# Create your views here.
