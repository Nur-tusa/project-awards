from django.urls import path
from django.contrib import admin
from . import views
from users import views as user_views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

urlpatterns=[
    path('profilelist/', views.profilelist, name='profile-list'),
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)