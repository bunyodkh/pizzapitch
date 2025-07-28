from django.contrib import admin
from unfold.admin import ModelAdmin

from .models import EventType, Event, Participant

@admin.register(EventType)
class EventTypeAdmin(ModelAdmin):
    pass

@admin.register(Event)
class EventAdmin(ModelAdmin):
    list_display = ('title', 'event_type', 'date', 'registration_deadline','is_active', 'registration_closed')

@admin.register(Participant)
class ParticipantAdmin(ModelAdmin):
    list_display = ('name', 'event', 'startup')
    list_filter = ('event', 'selected')
    search_fields = ('name', 'email', 'phone', 'tg', 'startup')

