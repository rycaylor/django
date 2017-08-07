# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from ..login.models import User
from dateutil.parser import parse
from datetime import datetime
# Create your models here.

class EventManager(models.Manager):
    def event_make(self, postData, user):
        results = {'create':True, 'error': [], 'event':None}
        if postData['event'] == '':
            results['create'] = False
            results['error'].append('Please enter an event type')
        else:
            event = postData['event']

        if postData['destination'] == '':
            results['create'] = False
            results['error'].append('Please enter a destination for your event')
        else:
            destination = postData['destination']

        if postData['description'] == '':
            results['create'] = False
            results['error'].append('Please enter a description so we know whats going to take place')
        else:
            description = postData['description']

        if postData['date_start'] == '':
            results['create'] = False
            results['error'].append('Please enter a starting date')
        else:
            date_start = datetime.strptime(postData['date_start'], '%Y-%m-%d').date()
        if postData['date_end'] == '':
            results['create'] = False
            results['error'].append('Please enter an ending date')
        else:
            date_end = datetime.strptime(postData['date_end'], '%Y-%m-%d').date()

        try:
            if date_start < datetime.now().date():
                results['create'] = False
                results['error'].append('Start date cannot occur before todays date')
            if date_end < date_start:
                results['create'] = False
                results['error'].append('End date cannot not occur before start date')
        except:
            pass

        if results['create']:
            user = User.objects.get(id = user)

            planned_event = Event.objects.create(destination=destination, event=event, description=description, date_start=date_start, date_end=date_end, maker_id=user.id)

            planned_event.save()
            results['event'] = planned_event
        return results










class Event(models.Model):
    destination = models.CharField(max_length=100)
    event = models.CharField(max_length=100)
    description = models.CharField(max_length=300)
    date_start = models.DateField()
    date_end = models.DateField()
    maker = models.ForeignKey(User, related_name='maker')
    goer = models.ManyToManyField(User, related_name='goer')
    objects = EventManager()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
