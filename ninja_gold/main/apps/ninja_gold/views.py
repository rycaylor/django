# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,redirect
import random
import datetime
# Create your views here.

def winlost():
    chance = random.randint(0,2)
    if chance == 1:
        return True
    else:
        return False

def addactivity(request, num, action, location):
    timestamp = datetime.datetime.now()
    if location == 'casino':
        if action == 'earned':
            earned = 'Earned %d from the casino %s' % (num,timestamp)
            request.session['activity'].insert(0,['earn',earned])
        elif action == 'lost':
            lost = 'Entered a casino and lost %d gold... Ouch %s' % (num, timestamp)
            request.session['activity'].insert(0,['lost', lost])
        else:
            print 'error'
    elif location == 'farm':
        request.session['activity'].insert(0,['earn', 'Earned %d from the %s! %s' % (num,location,timestamp)])
    elif location == 'cave':
        request.session['activity'].insert(0,['earn', 'Earned %d from the %s! %s' % (num,location,timestamp)])
    elif location == 'house':
        request.session['activity'].insert (0, ['earn', 'Earned %d from the %s! %s' % (num,location,timestamp)])
    else:
        print "error"


def index(request):
    try:
        request.session['num']
    except:
        request.session['num'] = 0
    try:
        request.session['activity']
    except:
        request.session['activity'] = []
    return render(request, 'ninja_gold/index.html')


def process(request):
    if request.method == 'POST':
        if request.POST['building'] == 'farm':
            farmn = random.randint(10,21)
            request.session['num'] += farmn
            addactivity(request, farmn, 'earned', 'farm')
        elif request.POST['building'] == 'cave':
            caven = random.randint(5,11)
            request.session['num'] += caven
            addactivity(request, caven, 'earned', 'cave')
        elif request.POST['building'] == 'house':
            housen = random.randint(2,6)
            request.session['num'] += housen
            addactivity(request, housen, 'earned', 'house')
        elif request.POST['building'] == 'casino':
            chance = winlost()
            casinon = random.randint(0,50)
            if chance == True:
                request.session['num'] += casinon
                addactivity(request, casinon, 'earned', 'casino')
            elif chance == False:
                request.session['num'] -= casinon
                addactivity(request, casinon, 'lost', 'casino')
        print request.session['num']

    return redirect('/')

def reset(request):
    request.session['num'] = 0
    request.session['activity'] = []
    return redirect ('/')
