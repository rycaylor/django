# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from ..login.models import User
from django.contrib import messages
from .models import Event

# Create your views here.
def index(request):
    if 'logged' not in request.session:
        return redirect('login:index')
    else:
        try:
            context = {
                    'user': User.objects.get(id=int(request.session['logged'])),
                    'events':Event.objects.all(),
                }
            return render(request, 'event/index.html', context)
        except:
            return redirect('login:index')


def add(request):
    if 'logged' not in request.session:
        return redirect('login:index')
    else:
        return render(request, 'event/add.html')

def make_event(request):
    user = int(request.session['logged'])
    event_valid = Event.objects.event_make(dict(request.POST.items()), user)
    if event_valid['create']:
        event = event_valid['event']
        messages.add_message(request, messages.INFO, 'Thanks for adding, ' + event.event  + ',  go back to the homepage to join other events or plan another event')
        return redirect('event:add')
    else:
        for error in event_valid['error']:
            messages.add_message(request, messages.INFO, error)
        return redirect('event:add')
