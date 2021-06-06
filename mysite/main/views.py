from django.http import HttpResponseRedirect, HttpResponse, response
from django.shortcuts import render
from django import forms
from .models import Profile, Education_level, Level

def index(response,id):
    prof = Profile.objects.get(id=id)
    # return HttpResponse("<h1>%s</h1><br><p>%s</p>" % (prof.name,prof.surname))
    return render(response,"main/base.html",{})

def home(response):
    return render(response, "main/home.html", {})


