from django.urls import path

app_name = 'events'

from .views import register_participant, show_participants


urlpatterns = [
    path('registration', register_participant, name='register-participant'),
    path('participants', show_participants, name='show-participants'),
]