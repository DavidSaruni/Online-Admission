from django.db import models

# Create your models here.
class UserList(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Item(models.Model):
    userlist = models.ForeignKey(UserList, on_delete=models.CASCADE)
    text = models.CharField(max_length=300)
    complete = models.BooleanField()

    def __str__(self):
        return self.text
    

class Admissions(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    religion = models.CharField(max_length=255)
    gender = models.CharField(max_length=255)
    dob = models.CharField(max_length=255)
    status = models.CharField(max_length=255)
    nationality = models.CharField(max_length=255)
    county = models.CharField(max_length=255)
    fname = models.CharField(max_length=255)
    fphone = models.CharField(max_length=255)
    femail = models.EmailField(max_length=255)
    foccupation = models.CharField(max_length=255)
    mname = models.CharField(max_length=255)
    mphone = models.CharField(max_length=255)
    memail = models.EmailField(max_length=255)
    moccupation = models.CharField(max_length=255)
    admdate = models.CharField(max_length=255)
    schoolname = models.CharField(max_length=255)
    grade = models.CharField(max_length=255)
    refno = models.CharField(max_length=255)
    
    def __str__(self):
        return self.name
    