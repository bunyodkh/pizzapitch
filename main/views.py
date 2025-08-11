from django.shortcuts import render

from events.forms import GuestRegistrationForm, ParticipantRegistrationForm
from events.models import Event
from mentors.models import Mentor
from partners.models import Partner


def index(request):
    active_event = Event.objects.filter(is_active=True).first()
    mentors = Mentor.objects.filter(show=True).order_by('name')
    partners = Partner.objects.filter(show=True).order_by('name')
    form = ParticipantRegistrationForm()
    guest_form = GuestRegistrationForm()
    return render(request, 'index.html', {
        'active_event': active_event,
        'form': form,
        'guest_form': guest_form,
        'mentors': mentors,
        'partners': partners
    })
