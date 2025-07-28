from django.urls import path

app_name = 'events'

from .views import register_participant


urlpatterns = [
    path('registration', register_participant, name='register-participant'),
]