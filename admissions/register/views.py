from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import RegisterForm
# Create your views here.
def register(response):
    if response.method == "POST":
        form = RegisterForm(response.POST)
        if form.is_valid():
            form.save()
            messages.success(response, "Sign Up Successful")
            return redirect("/login")
        else:
            messages.error(response, "Invalid Details")
            return render(response, "register/signup.html", {"form":form})
    else:  
        form = RegisterForm()      
        messages.error(response, "Invalid Details")
        return render(response, "register/signup.html", {"form":form})