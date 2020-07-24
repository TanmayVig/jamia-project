from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.views import generic
from django.http import Http404
from django.contrib.auth import get_user_model
from . import models
# Create your views here.

User=get_user_model()
class StudentListView(generic.ListView):
    model=User
    queryset=User.objects.all()
    template_name='Students/students_list.html'
class StudentDetail(generic.DetailView):
    model=models.User
    template_name='Students/students_detail.html'
