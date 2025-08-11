from django.contrib import admin
from unfold.admin import ModelAdmin

from .models import Event, EventType, Guest, Participant


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

@admin.register(Guest)
class GuestAdmin(ModelAdmin):
    list_display = ('name', 'event', 'phone', 'tg', 'created_at')
    list_filter = ('event', 'consent')
    search_fields = ('name', 'phone', 'tg')
