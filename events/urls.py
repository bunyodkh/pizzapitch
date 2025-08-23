from django.urls import path

app_name = 'events'

from .views import register_participant, show_participants, export_participants_to_excel


urlpatterns = [
    path('registration', register_participant, name='register-participant'),
    path('participants', show_participants, name='show-participants'),
    path('export-participants', export_participants_to_excel, name='export-participants-excel'),
]