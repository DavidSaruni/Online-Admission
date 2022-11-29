from django import forms
from django.contrib.auth.models import User
from .models import Admissions

class AdmissionForm(forms.Form):
    name = forms.CharField(max_length=255)
    phone = forms. CharField(max_length=255)
    email = forms.EmailField(max_length=255)
    religion = forms.CharField(max_length=255)
    gender = forms.CharField(max_length=255)
    dob = forms.CharField(max_length=255)
    status = forms.CharField(max_length=255)
    nationality = forms.CharField(max_length=255)
    county = forms.CharField(max_length=255)
    fname = forms.CharField(max_length=255)
    fphone = forms.CharField(max_length=255)
    femail = forms.EmailField(max_length=255)
    foccupation = forms.CharField(max_length=255)
    mname = forms.CharField(max_length=255)
    mphone = forms.CharField(max_length=255)
    memail = forms.EmailField(max_length=255)
    moccupation = forms.CharField(max_length=255)
    course = forms.CharField(max_length=255)
    admdate = forms.CharField(max_length=255)
    schoolname = forms.CharField(max_length=255)
    grade = forms.CharField(max_length=255)
    refno = forms.CharField(max_length=255)
    passport = forms.ImageField()
    idcard = forms.ImageField()
    birthcert = forms.FileField()
    cscert = forms.FileField()
    medcert = forms.FileField()
    holdername = forms.CharField(max_length=255)
    cardno = forms.CharField(max_length=255)
    cvcpwd = forms.CharField(max_length=255)
    expmonth = forms.CharField(max_length=255)
    expyear = forms.CharField(max_length=255)
    
    class Meta:
        model = Admissions
        fields = ["name","phone","email","religion","gender","dob","status","nationality",
        "county","fname","fphone","femail","foccupation","mname","mphone","memail","moccupation",
        "course","admdate","schoolname","grade","refno","passport","idcard","birthcert","cscert","medcert",
        "holdername","cardno","cvcpwd","expmonth","expyear"]
    
