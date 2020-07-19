import datetime


from django.db import models



class Schedule_class(models.Model):
    coid = models.AutoField(primary_key=True)
    name=models.CharField(max_length=50)
    faculty=models.CharField(max_length=50)
    date=models.DateField(default=datetime.date(2020,1,1))
    time=models.CharField(max_length=50)
    fee=models.IntegerField()
    duration=models.CharField(max_length=50)

class Student(models.Model):
    sname=models.CharField(max_length=50)
    contactno=models.IntegerField()
    email=models.EmailField()
    password=models.CharField(max_length=50)

class Entrol(models.Model):
     contact = models.IntegerField()
     course = models.IntegerField()




