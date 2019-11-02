from django.shortcuts import render
import requests
from django.http import HttpResponse
# Create your views here.

def index(request):
    
    return HttpResponse(requests.get('https://api.github.com'))