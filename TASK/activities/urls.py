from django import urls
from . import views
from django.urls import path

app_name = 'activities'

urlpatterns = [
    path("", views.index, name = 'index'),
    path("add", views.add, name = 'add'),
]