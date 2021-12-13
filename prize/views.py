from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse, Http404, HttpResponseRedirect, JsonResponse
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.views import generic
from django.db.models import F
from users.models import Profile
from . models import Project, ProjectVote
from django.contrib.auth.models import User
from .forms import *
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializer import ProfileSerializer, ProjectSerializer
from rest_framework import status
from .permissions import IsAdminOrReadOnly


def welcome(request):
    one_entry = Project.objects.filter(id=1)
    two_entry = Project.objects.filter(pk=2)
    three_entry = Project.objects.filter(id=3)
    four_entry = Project.objects.filter(id=4)
    five_entry = Project.objects.filter(id=3)

    return render(request, 'awwards/welcome.html', {"one_entry":one_entry, "two_entry":two_entry, "three_entry":three_entry, "four_entry":four_entry, "five_entry":five_entry})

def home(request):
    current_user = request.user
    projects = Project.objects.all()
    users = Profile.objects.all()

    form = ReviewForm()

    return render(request, 'prize/index.html', {'projects':projects,'current_user':current_user,'users':users,'form':form})
