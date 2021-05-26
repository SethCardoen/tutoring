from django.db import models

class Education_level(models.Model):
    diploma = models.CharField(max_length=200)

class User(models.Model):
    name = models.CharField('Name', max_length=200)
    surname = models.CharField('Surname', max_length=200)
    birthdate = models.DateField('enter your birthdate')
    education_level = models.ForeignKey(Education_level, on_delete=models.CASCADE)




