from django.db import models
from django.contrib.auth.models import User

class Account(models.Model):
    email_address = models.CharField(max_length=100)
    student_ID = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    student_name = models.CharField(max_length=100)
    year_level = models.CharField(max_length=100)

    def __str__(self):
        return self.student_name

class Subjects(models.Model):
    subject_code = models.CharField(max_length=100)
    subject_name = models.CharField(max_length=100)
    units = models.IntegerField()
    timedays = models.CharField()
    professor_name = models.CharField(max_length=100)

    def __str__(self):
        return self.subject_code

class Personal_Information(models.Model):
    gender_choices = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='personal_information', null=True)
    student_Id = models.CharField(max_length=100)
    lrn = models.IntegerField()
    gender = models.CharField(max_length=1, choices=gender_choices)
    phone_number = models.IntegerField()
    address = models.CharField(max_length=100)

    def __str__(self):
        return self.student_Id
   

class Programs(models.Model):
    department_code = models.CharField(max_length=100)
    department_name = models.CharField(max_length=100)
    proram_head = models.CharField(max_length=100)
    program_descriptions = models.CharField(max_length=1000)
    schedule = models.CharField(max_length=100)

    def __str__(self):
        return self.department_code
   
  
class Teachers(models.Model):
    gender_choices = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('o', 'Other'),
    ]
    name = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    year = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    gender = models.CharField(max_length=1, choices=gender_choices)

    def __str__(self):
        return self.name

