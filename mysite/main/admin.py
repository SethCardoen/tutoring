from django.contrib import admin
from .models import Profile, Education_level, Level, Appointment, ToDoList, Item

admin.site.register(Profile)
admin.site.register(Education_level)
admin.site.register(Level)
admin.site.register(Appointment)
admin.site.register(ToDoList)
admin.site.register(Item)
