from django.shortcuts import render
import os
import http.cookies as cookies
import requests
from django.http import HttpResponse
import websockets
import PyChromeDevTools as devtools
import time

# Create your views here.
def displayCookies(request):
    try:
        #cookieObjects = []

        chrome = devtools.ChromeInterface()
        chrome.Network.enable()
        chrome.Page.enable()

        #chrome.Page.navigate(url="http://www.nytimes.com/")
        #chrome.wait_event("Page.frameStoppedLoading", timeout=60)

        time.sleep(5)

        cookieList = chrome.Network.getCookies()
        #cookieList = cookieList.split('; ')

        #for cookie in cookieList:
        #    c = cookies.SimpleCookie()
        #    c.load(cookie)
        #    cookieObjects.append(c)

        #print(cookieObjects)

        return HttpResponse("Number of cookies returned:\n", len(cookieList))
        #return HttpResponse("Cookies returned:\n", cookieList)
    except requests.exceptions.ConnectionError:
        return HttpResponse("Connection refused")