from django.urls import path

from . import views

urlpatterns = [
    path('<int:id>', views.index, name="index"),
    path("", views.home, name="home"),
    path("admissions/", views.admissions, name="admissions"),
    path("admissions_save/", views.admissions_save, name="admissions_save"),
]