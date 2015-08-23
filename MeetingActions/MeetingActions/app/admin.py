from django.contrib import admin
from .models import Topic, Meeting, Action

class Meetinginline(admin.StackedInline):
    model = Meeting
    extra = 3

class TopicAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,              {'fields': ['topic_name']}),
        ('Topic Detail',    {'fields': ['topic_desc'], 'classes': ['collapse'] })
    ]
    inlines = [Meetinginline]

#        ('Topic Destail',   {'fields':['topic_desc'], 'classes': ['collapse'] })]

admin.site.register(Topic, TopicAdmin)


class Actioninline(admin.TabularInline):
    model=Action
    extra=10
    list_display = ('action_description', 'action_assignee', 'action_duedate', 'action_status') 

class MeetingAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,          {'fields': ['meeting_topic']}),
        ('Date',        {'fields': ['meeting_date']})
    ]    
    inlines = [Actioninline]

admin.site.register(Meeting, MeetingAdmin)

class ActionAdmin(admin.ModelAdmin):
    list_display = ('action_description', 'action_topic', 'action_assignee', 'action_duedate', 'action_status') 
    list_filter = ['action_status', 'action_topic', 'action_assignee']

admin.site.register(Action, ActionAdmin)
