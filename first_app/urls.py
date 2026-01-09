from django.urls import path
from . import views
urlpatterns = [
    path('',views.Home.as_view(),name='home'),
    path('contact/',views.contact_view, name = 'contact'),
    path('about/', views.About.as_view(),name = 'about'),
    path('studio/',views.Studio.as_view(), name = 'studio'),
    path('work/',views.Work.as_view(), name = 'work'),
    path('work/web1', views.Web1.as_view(), name = 'web1'),
    path('work/web2', views.Web1.as_view(), name='web2'),
    path('work/web3', views.Web1.as_view(), name='web3'),
    path('work/web4', views.Web1.as_view(), name='web4'),

]