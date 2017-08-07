# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from .models import Secret, Like
from ..login.models import User
from django.contrib import messages
from django.db.models import Count
# Create your views here.

def index(request):
    if 'logged' not in request.session:
        return redirect('login:index')
    else:
        try:
            context = {
                    'user': User.objects.get(id=int(request.session['logged'])),
                    'secrets': Secret.objects.all(),
                    'like' : Like.objects.all()
                }
            return render(request, 'dojo_secret/index.html', context)
        except:
            return redirect('login:index')

def post(request):
    if 'logged' not in request.session:
        return redirect('login:index')
    else:
        try:
            user = int(request.session['logged'])
            secret_valid = Secret.objects.make_secret(dict(request.POST.items()), user)
            if secret_valid['create']:
                secret = secret_valid['content']
                return redirect('ds:index')
            else:
                for error in secret_valid['errors']:
                    messages.add_message(request, messages.INFO, error)
                    return redirect('ds:index')
        except:
            return redirec('login:index')
def like(request, id):
    if 'logged' not in request.session:
        return redirect('login:index')
    user = int(request.session['logged'])
    temp = int(id)
    like_inc = Like.objects.make_like(user, temp)
    return redirect('ds:index')


def unlike(request, id):
    if 'logged' not in request.session:
        return redirect('login:index')
    user = int(request.session['logged'])
    temp = int(id)
    unlike_rev = Like.objects.make_unlike(user, temp)
    return redirect('ds:index')

def delete(request, id):
    if 'logged' not in request.session:
        return redirect('login:index')
    user = int(request.session['logged'])
    temp = int(id)
    make_delete = Secret.objects.make_delete(user, temp)
    return redirect('ds:index')


def mostpopular(request):
    if 'logged' not in request.session:
        return redirect('login:index')
    context = {
        'secrets': Secret.objects.annotate(num_likes=Count("sec")).order_by('-num_likes'),
        'user': User.objects.get(id=int(request.session['logged'])),
        'like' : Like.objects.all(),
        }
    return render(request, 'dojo_secret/popular.html', context)
