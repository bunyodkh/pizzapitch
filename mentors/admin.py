from django.contrib import admin
from unfold.admin import ModelAdmin

from .models import Mentor

@admin.register(Mentor)
class MentorAdmin(ModelAdmin):
    list_display = ('name', 'email', 'phone', 'position')
    search_fields = ('name', 'email', 'phone', 'position')
    list_filter = ('created_at', 'updated_at')
    ordering = ('name',)
    list_per_page = 20
