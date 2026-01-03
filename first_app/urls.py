from django.urls import path
from . import views
urlpatterns = [
    path('',views.Home.as_view(),name='home'),
    path('contact/',views.contact_view, name = 'contact')

]