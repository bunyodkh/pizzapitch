from django.shortcuts import render, redirect
from django.contrib import messages
from django.utils.translation import gettext as _

import openpyxl
from django.http import HttpResponse

from .models import Event
from .forms import ParticipantRegistrationForm
from django.contrib.auth.decorators import login_required


def register_participant(request):
    active_event = Event.objects.filter(is_active=True).first()

    if request.method == 'POST':
        form = ParticipantRegistrationForm(request.POST)

        if form.is_valid():
            participant = form.save(commit=False)
            participant.event = active_event
            participant.save()
            messages.success(request, "success")
            return redirect(request.path)
    else:
        form = ParticipantRegistrationForm()
    return render(request, 'index.html', {
        'form': form,
        'active_event': active_event,
    })


@login_required
def show_participants(request):
    active_event = Event.objects.filter(is_active=True).first()
    registered_people = active_event.participant_set.all() if active_event else []
    return render(request, 'participants.html', {
        'registered_people': registered_people,
        'active_event': active_event,
    }) 

import io

@login_required
def export_participants_to_excel(request):
    active_event = Event.objects.filter(is_active=True).first()
    registered_people = active_event.participant_set.all() if active_event else []

    workbook = openpyxl.Workbook()
    sheet = workbook.active
    sheet.title = "Participants"

    headers = ["Name", "Phone", "Telegram", "Startup", "Description", "Presentation Link", "Consent", "Selected"]
    sheet.append(headers)

    for participant in registered_people:
        sheet.append([
            participant.name,
            participant.phone,
            participant.tg,
            participant.startup,
            participant.startup_description,
            participant.presentation_link,
            participant.consent,
            participant.selected
        ])

    buffer = io.BytesIO()
    workbook.save(buffer)
    buffer.seek(0)

    response = HttpResponse(
        buffer.getvalue(),
        content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
    )
    response['Content-Disposition'] = 'attachment; filename=participants.xlsx'
    return response