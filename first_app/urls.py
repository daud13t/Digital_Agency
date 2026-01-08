from django.urls import path
from . import views
urlpatterns = [
    path('',views.Home.as_view(),name='home'),
    path('contact/',views.contact_view, name = 'contact'),
    path('about/', views.About.as_view(),name = 'about'),
    path('studio/',views.Studio.as_view(), name = 'studio'),
    path('work/',views.Work.as_view(), name = 'work'),
]