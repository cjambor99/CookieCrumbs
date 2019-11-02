from django.shortcuts import render
import os
import http.cookies as cookies
import requests
from django.http import HttpResponse

# Create your views here.
def displayCookies(request):
    print("Content-type: text/html\n\n")

    #print("""
    #<html>
    #<body>
    #<h1>Display cookies</h1>
    #""")

    if 'HTTP_COOKIE' in os.environ:
        cookieList = os.environ['HTTP_COOKIE']
        print(cookieList)

        cookieList = cookieList.split('; ')
        print(cookieList)

        for cookie in cookieList:
            c = cookies.SimpleCookie()
            c.load(cookie)
            print(c)

    #print("""
    #</body>
    #</html>
    #""")

    return HttpResponse("Cookies returned")