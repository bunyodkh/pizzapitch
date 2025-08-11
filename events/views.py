from django.contrib import messages
from django.shortcuts import redirect, render
from django.utils.translation import gettext as _

from .forms import GuestRegistrationForm, ParticipantRegistrationForm
from .models import Event


def register_participant(request):
    active_event = Event.objects.filter(is_active=True).first()

    if request.method == 'POST':
        form = ParticipantRegistrationForm(request.POST)

        if form.is_valid():
            print('REGISTRATION FORM VALID')
            participant = form.save(commit=False)
            participant.event = active_event
            participant.save()
            messages.success(request, _("Мы получили вашу заявка на участие! Спасибо за интерес. Мы с вами свяжемся."))
            return redirect(request.path)
    else:
        form = ParticipantRegistrationForm()
    return render(request, 'index.html', {
        'form': form,
        'active_event': active_event,
    })


def register_guest(request):
    active_event = Event.objects.filter(is_active=True).first()

    if request.method == 'POST':
        guest_form = GuestRegistrationForm(request.POST)

        if guest_form.is_valid():
            print('GUEST REGISTRATION FORM VALID')
            guest = guest_form.save(commit=False)
            guest.event = active_event
            guest.save()
            messages.success(request, _("Спасибо за регистрацию! Мы свяжемся с вами перед мероприятием."))
            return redirect('main:index')
    else:
        guest_form = GuestRegistrationForm()

    return render(request, 'index.html', {
        'guest_form': guest_form,
        'active_event': active_event,
    })
