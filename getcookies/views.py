# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.template import loader 

# Create your views here.
from django.http import HttpResponse, Http404

def index(request):
    return render(request, 'getcookies/index.html')

