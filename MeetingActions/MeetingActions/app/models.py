"""
Definition of models.
"""

from django.db import models
from datetime import datetime

# Create your models here.
class Topic(models.Model):
    topic_name = models.CharField(max_length=80, )
    topic_desc = models.CharField(max_length=200)
    topic_createdate = models.DateTimeField('date_published')

    def __str__(self):
        return self.topic_name

class Meeting(models.Model):
    meeting_date = models.DateTimeField('date_published')
    meeting_topic = models.ForeignKey(Topic)

    def __str__(self):
        return self.meeting_date.__str__()

cOPEN = 'OPEN'
cCLOSED= 'CLOSED'

STATUS_CHOICES = (
    (cOPEN, 'Open'),
    (cCLOSED, 'Closed')
    )

class Action(models.Model):
    action_description = models.TextField(max_length=200)
    action_assignee = models.CharField(max_length=30)
    action_createdate = models.DateTimeField('date_published')
    action_duedate = models.DateTimeField() 
    action_topic = models.ForeignKey(Topic)
    action_Meeting = models.ForeignKey(Meeting)
    action_status = models.CharField(max_length=30,choices=STATUS_CHOICES, default=cOPEN)

    def __str__(self):
        return self.action_description
