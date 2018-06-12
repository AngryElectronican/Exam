from django.conf.urls import url
from django.contrib import admin
from .views import Registration

urlpatterns = [
    url(r'^register', Registration,name="Registration"),
]