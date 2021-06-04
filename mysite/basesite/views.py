from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Profile

def homeview(response):
   # p = Profile.objects.get(id=id)
   # for item in Profile.item_set.all():

    fullname = "id =" + p.name
    return render(response, "basesite/home.html", {"fullname": fullname})

def profileview(request, profile_id):
    return HttpResponse("You're looking at the profile of %s." % profile_id)

def searchview(request, profile_id):
    response = "You're looking at the searchview of %s."
    return HttpResponse(response % profile_id)

def notesview(request, profile_id):
    return HttpResponse("You're looking at the notes of %s." % profile_id)

