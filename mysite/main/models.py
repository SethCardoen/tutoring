from django.db import models
from datetime import date
from django.utils import timezone

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
        return self.name + self.id
        #return render(response, "main/base.html", {"fullname": fullname})







