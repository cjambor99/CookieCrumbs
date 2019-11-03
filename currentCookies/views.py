from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
import PyChromeDevTools as pyChrome

#might be good to use browsercookie library - functionality for returning local cookies on firefox and chrome
#depends on a pycrypto library that requires C++, no time to install
def currentCookies(request):
    return HttpResponse("This page should display cookies stored locally in browser")