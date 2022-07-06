
from django.contrib import admin
from django.urls import path
from AppFamilia import views


urlpatterns = [
    path('familia/', views.familia),
]
