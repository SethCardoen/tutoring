from django.db import models
from datetime import date
from django.utils import timezone
from django.contrib.auth.models import User

class Education_level(models.Model):
    diploma = models.CharField(max_length=200)

    def __str__(self):
        return self.diploma

class Level(models.Model):
    rank = models.CharField('Priviliges', max_length=200, blank=True, null=True)

    def __str__(self):
        return self.rank

class Profile(models.Model):
    name = models.CharField('Name', max_length=200)
    surname = models.CharField('Surname', max_length=200)
    birthdate = models.DateField('enter your birthdate')
    education_level = models.ForeignKey(Education_level, on_delete=models.CASCADE)
    sign_in_date = models.DateField(auto_now_add=True)
    level = models.ForeignKey(Level, on_delete=models.CASCADE, blank=True, null=True)
   # fullname = str(name) + str(surname)

    def lenght_of_using_the_platform(self):
        loutp = date.today() - self.sign_in_date

    def __str__(self):
        return self.name
        #return render(response, "main/base.html", {"fullname": fullname})


class Appointment(models.Model):
    code = models.CharField('Code', max_length=200)
    teacher =  models.ForeignKey(Profile, on_delete=models.CASCADE)
    schedule =  models.DateTimeField()

    def __str__(self):
        return self.code


# Create your models here.
class ToDoList(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="todolist",null=True)
    date = models.DateTimeField("date published", auto_now_add=True)
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Item(models.Model):
    text = models.CharField(max_length=500)
    toDoList = models.ForeignKey(ToDoList, on_delete=models.CASCADE)
    complete = models.BooleanField()

    def __str__(self):
        return self.text
