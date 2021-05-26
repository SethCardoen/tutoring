from django.db import models
from datetime import date
from django.utils import timezone

class Education_level(models.Model):
    diploma = models.CharField(max_length=200)

    def __str__(self):
        return self.Education_level_text

class User(models.Model):
    name = models.CharField('Name', max_length=200)
    surname = models.CharField('Surname', max_length=200)
    birthdate = models.DateField('enter your birthdate')
    education_level = models.ForeignKey(Education_level, on_delete=models.CASCADE)
    sign_in_date = models.DateField(auto_now=True)

    def lenght_of_using_the_platform(self):
        loutp = date.today() - self.sign_in_date
        print(loutp)

    def __str__(self):
        return self.User_text




