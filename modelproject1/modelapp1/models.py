from django.db import models

class Student(models.Model):
    sno=models.IntegerField()
    sname=models.CharField(max_length=35)
    srollno=models.IntegerField()
    csr=models.CharField(max_length=25)
    cname=models.CharField(max_length=20)


