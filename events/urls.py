from django.urls import path

app_name = 'events'

from .views import show_participants, export_participants_to_excel, standard_registration, premium_registration, guest_registration


urlpatterns = [
    path('registration/standard/', standard_registration, name='standard-registration'),
    path('registration/premium/', premium_registration, name='premium-registration'),
    path('participants', show_participants, name='show-participants'),
    path('export-participants', export_participants_to_excel, name='export-participants-excel'),
    path('registration/guest/', guest_registration, name='guest-registration'),
]