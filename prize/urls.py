from django.conf.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
  path('welcome', views.welcome, name = 'awwards-welcome'),

  path("",views.index,name="home")
]