from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import UserList, Item, Admissions
from django.contrib import messages
from .forms import AdmissionForm
# Create your views here.
def index(response, id):
    adm = UserList.objects.get(id=id)
    item = adm.item_set.get(id=1)
    return HttpResponse("<h1>Student admissions working for %s</h1><br><p>%s</p>" %(adm.name, str(item.text)))

def home(response):
    return render(response, "main/home.html", {})

def admissions(request):
    return render(request, "main/main.html")

# def admissions_save(request):
    # if request.method=="POST":
    #     admission = admissions(request.POST.get)
    #     if admission.is_valid():
    #         admission.save()
    #         messages.success(request, "Success")
    #         return redirect("/admissions")
    #     else:
    #         messages.error(request, "Invalid")
    #         return render(request, "main/main.html", {"admissions":admission})
    # else:
    #     admission = admissions()
    #     messages.error(request, "Invalid Details")
    #     return render(request, "main/main.html", {"admission":admission})
def admissions_save(request):
    
    if request.method =="GET":
        return HttpResponseRedirect(reverse("admissions"))
    elif request.method == "POST":
        admissions = Admissions()
        form = AdmissionForm(request.POST, request.FILES)
        if form.is_valid():
            admissions.name=form.cleaned_data.get("name")
            admissions.phone=form.cleaned_data.get("phone")
            admissions.email=form.cleaned_data.get("email")
            admissions.religion=form.cleaned_data.get("religion")
            admissions.gender=form.cleaned_data.get("gender")
            admissions.dob=form.cleaned_data.get("dob")
            admissions.status=form.cleaned_data.get("status")
            admissions.nationality=form.cleaned_data.get("nationality")
            admissions.county=form.cleaned_data.get("county")
            admissions.fname=form.cleaned_data.get("fname")
            admissions.fphone=form.cleaned_data.get("fphone")
            admissions.femail=form.cleaned_data.get("femail")
            admissions.foccupation=form.cleaned_data.get("foccupation")
            admissions.mname=form.cleaned_data.get("mname")
            admissions.mphone=form.cleaned_data.get("mphone")
            admissions.memail=form.cleaned_data.get("memail")
            admissions.moccupation=form.cleaned_data.get("moccupation")
            admissions.course=form.cleaned_data.get("course")
            admissions.admdate=form.cleaned_data.get("admdate")
            admissions.schoolname=form.cleaned_data.get("schoolname")
            admissions.grade=form.cleaned_data.get("grade")
            admissions.refno=form.cleaned_data.get("refno")
            admissions.passport=form.cleaned_data.get("passport")
            admissions.idcard=form.cleaned_data.get("idcard")
            admissions.birthcert=form.cleaned_data.get("birthcert")
            admissions.cscert=form.cleaned_data.get("cscert")
            admissions.medcert=form.cleaned_data.get("medcert")
            admissions.holdername=form.cleaned_data.get("holdername")
            admissions.cardno=form.cleaned_data.get("cardno")
            admissions.cvcpwd=form.cleaned_data.get("cvcpwd")
            admissions.expmonth=form.cleaned_data.get("expmonth")
            admissions.expyear=form.cleaned_data.get("expyear")
            admissions.save()
            messages.success(request,"Data Saved Successfully")
            return HttpResponseRedirect(reverse("admissions"))
        else:
            messages.error(request,"Error Saving Data")
            return HttpResponseRedirect(reverse("admissions"))
    else:
        return HttpResponseRedirect(reverse("admissions"))

       

    
        
        
    

