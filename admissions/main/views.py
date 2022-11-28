from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import UserList, Item, Admissions
from django.contrib import messages
# Create your views here.
def index(response, id):
    adm = UserList.objects.get(id=id)
    item = adm.item_set.get(id=1)
    return HttpResponse("<h1>Student admissions working for %s</h1><br><p>%s</p>" %(adm.name, str(item.text)))

def home(response):
    return render(response, "main/home.html", {})

def admissions(request):
    return render(request, "main/main.html", {})

def admissions_save(request):
    if request.method!="POST":
        return HttpResponseRedirect(reverse("admissions"))
    else:
        name=request.POST.get("name")
        phone=request.POST.get("phone")
        email=request.POST.get("email")
        religion=request.POST.get("religion")
        gender=request.POST.get("gender")
        dob=request.POST.get("dob")
        status=request.POST.get("status")
        nationality=request.POST.get("nationality")
        county=request.POST.get("county")
        fname=request.POST.get("fname")
        fphone=request.POST.get("fphone")
        femail=request.POST.get("femail")
        foccupation=request.POST.get("foccupation")
        mname=request.POST.get("mname")
        mphone=request.POST.get("mphone")
        memail=request.POST.get("memail")
        moccupation=request.POST.get("moccupation")
        course=request.POST.get("course")
        admdate=request.POST.get("admdate")
        schoolname=request.POST.get("schoolname")
        grade=request.POST.get("grade")
        refno=request.POST.get("refno")
        try:
            admission =  Admissions(name=name,phone=phone,email=email,
                                religion=religion,gender=gender,dob=dob,
                                status=status,nationality=nationality,county=county,
                                fname=fname,fphone=fphone,femail=femail,
                                foccupation=foccupation,mname=mname,mphone=mphone,
                                memail=memail,moccupation=moccupation,course=course,
                                admdate=admdate,schoolname=schoolname,grade=grade,refno=refno
                                )
            admission.save()
            messages.success(request,"Data Saved Successfully")
            return render(request, "main/main.html", {})
        except:
            messages.error(request,"Error Saving Data")
            return render(request, "main/main.html", {})
        
    

