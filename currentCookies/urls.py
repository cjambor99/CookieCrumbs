from . import views
from django.conf.urls import url, include

urlpatterns = [
    url(r'', views.currentCookies, name='currentCookies'),
]