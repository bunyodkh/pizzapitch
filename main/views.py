from django.shortcuts import render

from events.models import Event
from mentors.models import Mentor
from partners.models import Partner
from events.forms import ParticipantRegistrationForm


def index(request):
    active_event = Event.objects.filter(is_active=True).first()
    mentors = Mentor.objects.filter(show=True).order_by('name')
    partners = Partner.objects.filter(show=True).order_by('name')
    form = ParticipantRegistrationForm(initial={'registration_type': 'standard'})
    return render(request, 'index.html', {'active_event': active_event, 'form': form, 'mentors': mentors, 'partners': partners})
