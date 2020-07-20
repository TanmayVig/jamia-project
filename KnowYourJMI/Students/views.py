from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.views import generic
from django.http import Http404
from django.contrib.auth import get_user_model
from . import models
# Create your views here.

User=get_user_model()
class StudentList(generic.ListView):
    model=models.Students
class StudentDetail(generic.DetailView):
    model=models.Students
