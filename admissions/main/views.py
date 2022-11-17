from django.shortcuts import render
from django.http import HttpResponse
from .models import UserList, Item
# Create your views here.
def index(response, id):
    adm = UserList.objects.get(id=id)
    item = adm.item_set.get(id=1)
    return HttpResponse("<h1>Student admissions working for %s</h1><br><p>%s</p>" %(adm.name, str(item.text)))

def admissions(request):
    return render(request, "main/main.html", {})

