from django.http import HttpResponseRedirect, HttpResponse, response
from django.shortcuts import render
from django import forms
from .models import Profile, Education_level, Level, Appointment, ToDoList, Item
from .forms import CreateNewList

def index(response,id):
    #prof = Profile.objects.get(id=id)
    #app = {"test1", "test34"}
    #for item in Appointment.objects.get(teacher=id):
    #return HttpResponse("<h1> %s </h1>" % (ls.name))
    # return HttpResponse("<h1>%s</h1><br><p>%s</p>" % (prof.name,prof.surname,str(app)))
    # return render(response,"main/list.html",{"prof":prof,"app":app})

    ls = ToDoList.objects.get(id=id)

    if response.method == "POST":
        print(response.POST)
        if response.POST.get("save"):
            for item in ls.item_set.all():
                if response.POST.get("c" +  str(item.id)) == "clicked":
                    item.complete = True
                else:
                    item.complete = False
            item.save()

        elif response.POST.get("newItem"):
            txt = response.POST.get("new")

            if len(txt) > 2:
                ls.item_set.create(text=txt, complete=False)
            else:
                print("invalid ")




    return render(response,"main/list.html",{"ls":ls})


def home(response):
    return render(response, "main/home.html", {"name":"test"})

def create(response):
    if response.method == "POST":
        form = CreateNewList(response.POST)

        if form.is_valid():
            n = form.cleaned_data["name"]
            t = ToDoList(name=n)
            t.save()

        return HttpResponseRedirect("/%i" %t.id)

    else:
        form = CreateNewList()
    return render(response, "main/create.html",{"form":form})