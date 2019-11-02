from django.shortcuts import render
from django.http import HttpResponse
import PyChromeDevTools as pyChrome
import time
# Create your views here.

def index(request):
    
    chrome = pyChrome.ChromeInterface()
    chrome.Network.enable()
    chrome.Page.enable()

    chrome.Page.navigate(url="https://www.google.com/")
    chrome.wait_event("Page.frameStoppedLoading",timeout=60)

    #time.sleep(2)

    cookies = chrome.Network.getCookies()
    #request.session['uid'] = cookies
    print(cookies)
    #theUrl="http://127.0.0.1:8000/display?cook=".append(cookies)
    newstr = " ".join(("http://127.0.0.1:8000/displayCookies?cookieList=", str(cookies)))
    print(newstr)
    chrome.Page.navigate(url=newstr)

    return HttpResponse("")