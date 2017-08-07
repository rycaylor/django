# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from .models import Booker
# Create your views here.


def index(request):
    context = {

    'show' : Booker.objects.all()

    }



    return render(request, 'add_book/index.html', context)


def show(request):
    Booker.objects.create(title=request.POST['title'], author=request.POST['author'], category=request.POST['category'])
    return redirect('/')
