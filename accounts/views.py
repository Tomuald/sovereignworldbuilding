# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.urls import reverse_lazy
from django.views.generic.edit import CreateView

from .forms import CustomUserCreationForm

class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

def sign_up_or_in(request):
    pass
    #form =
