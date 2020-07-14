from django.shortcuts import render
from django.views import generic
from . import forms
from django.urls import reverse_lazy
# Create your views here.

class Signup(generic.CreateView):
    form_class=forms.userCreateForm
    success_url=reverse_lazy('login')
    template_name='accounts/signup.html'
    
