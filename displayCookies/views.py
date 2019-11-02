from django.shortcuts import render
from django.http import HttpResponse, Http404

# Create your views here.
def displayCookies(request):
    cookieList = request.GET.get('cookieList')
    return HttpResponse("Cookie list: " + str(cookieList))