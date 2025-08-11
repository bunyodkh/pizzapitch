from django.urls import path

app_name = 'events'

from .views import register_guest, register_participant

urlpatterns = [
    path('registration', register_participant, name='register-participant'),
    path('guest-registration', register_guest, name='register-guest'),
]
