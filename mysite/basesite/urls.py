from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),   #with the index, we can call index from everywhere
]