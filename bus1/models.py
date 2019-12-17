from django.db import models
from random import *
class faculty(models.Model):
   
    faculty_name=models.CharField(max_length=100,default='plz give full name')
    subject=models.CharField(max_length=100)
    department=models.CharField(max_length=100)
    qualification=models.CharField(max_length=100)
    experience=models.CharField(max_length=100)
    
    email=models.EmailField()
   
class student(models.Model):
      u=''
      for i in range(0,4):
         u=u+str(randint(0,9))
      student_name=models.CharField(max_length=100,default='plz give full name')
      branch=models.CharField(max_length=100)
      year=models.CharField(max_length=4)
      email=models.EmailField()
      student_id=models.IntegerField(default=u)
class studentfake(models.Model):
      student_ID=models.IntegerField()
      branch=models.CharField(max_length=100)

    

  
