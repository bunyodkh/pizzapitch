from django.shortcuts import render, redirect
from django.contrib import messages
from django.utils import translation
from django.utils.translation import gettext as _

from .models import Event
from .forms import ParticipantRegistrationForm



def register_participant(request):
    active_event = Event.objects.filter(is_active=True).first()

    user_language = request.LANGUAGE_CODE  
    translation.activate(user_language)

    if request.method == 'POST':
        form = ParticipantRegistrationForm(request.POST)

        if form.is_valid():
            participant = form.save(commit=False)
            participant.event = active_event
            participant.save()
            messages.success(request, "registration_received")
            return redirect(request.path)
    else:
        form = ParticipantRegistrationForm()
    return render(request, 'index.html', {
        'form': form,
        'active_event': active_event,
    })