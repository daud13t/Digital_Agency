from django.urls import path
from . import views

urlpattern = [
    path('',views.Home.as_view(),name="home")
]