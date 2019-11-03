from django.shortcuts import render
from django.http import HttpResponse, Http404
import http.cookies as cookies
import json

# Create your views here.
def displayCookies(request):
    cookieList = request.GET.get('cookieList')
    cookieObjects = []
    cookieDump = eval(cookieList)

    for cookie in cookieDump['result']['cookies']:
       cookieObjects.append(cookie)
      
    #cookieObjects.append(cookieObjects)

    cookieObjects.append('Test')

    return render(request, 'cookieCrumbs/display.html', {'cookieObjects':cookieObjects})