from django.contrib import admin
from unfold.admin import ModelAdmin

from .models import Partner

@admin.register(Partner)
class PartnerAdmin(ModelAdmin):
    list_display = ('name', 'website')
    search_fields = ('name',)
    list_filter = ('created_at', 'updated_at')
