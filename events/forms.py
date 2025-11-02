from django import forms
from django.utils.translation import gettext_lazy as _

from .models import Participant, Guest


class ParticipantRegistrationForm(forms.ModelForm):
    class Meta:
        model = Participant
        fields = ['name', 'phone', 'tg', 'startup', 'startup_description', 'presentation_link', 'participants_consent', 'registration_type']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'input', 'id':'start-registration', 'placeholder': _('Ваше имя')}),
            'phone': forms.TextInput(attrs={'class': 'input', 'placeholder': _('Ваш телефон')}),
            'tg': forms.TextInput(attrs={'class': 'input', 'placeholder': _('Ваш ник в Телеграм')}),
            'startup': forms.TextInput(attrs={'class': 'input', 'placeholder': _('Название вашего стартапа')}),
            'startup_description': forms.Textarea(attrs={'class': 'input', 'placeholder': _('Краткое описание вашего стартапа')}),
            'presentation_link': forms.TextInput(attrs={'class': 'input', 'placeholder': _('Ссылка на презентацию')}),
            'participants_consent': forms.Select(attrs={'class': 'input'}),
            'registration_type': forms.HiddenInput(),
        }
        labels = {
            'name': _('Полное имя'),
            'phone': _('Номер телефона'),
            'tg': _('Телеграм ник'),
            'startup': _('Название стартапа'),
            'startup_description': _('Краткая информация о стартапе'),
            'presentation_link': _('Ссылка на презентацию'),
            'participants_consent': _('Согласны ли вы со съемкой вашей презентации, публикацией информации о вашем стартапе и делиться своими контактами с партнерами проекта и заинтересованными сторонами?'),
            'registration_type': _('Тип регистрации'),
        }

    
    def clean_name(self):
        name = self.cleaned_data.get('name')
        if not name or not str(name).strip():
            raise forms.ValidationError(_("Полное имя обязательно."))
        return str(name).strip()
    
    def clean_phone(self):
        phone = self.cleaned_data.get('phone')
        if not phone or not str(phone).strip():
            raise forms.ValidationError(_("Номер телефона обязателен."))
        return str(phone).strip()
    
    def clean_tg(self):
        tg = self.cleaned_data.get('tg')
        if not tg or not str(tg).strip():
            raise forms.ValidationError(_("Телеграм ник обязателен."))
        return str(tg).strip()
    
    def clean_startup(self):
        startup = self.cleaned_data.get('startup')
        if not startup or not str(startup).strip():
            raise forms.ValidationError(_("Название стартапа обязательно."))
        return str(startup).strip()
    
    def clean_startup_description(self):
        startup_description = self.cleaned_data.get('startup_description')
        if not startup_description or not str(startup_description).strip():
            raise forms.ValidationError(_("Краткое описание стартапа обязательно."))
        return str(startup_description).strip()
    
    def clean_presentation_link(self):
        presentation_link = self.cleaned_data.get('presentation_link')
        if not presentation_link or not str(presentation_link).strip():
            raise forms.ValidationError(_("Ссылка на презентацию обязательна."))
        return str(presentation_link).strip()
    
    def clean_participants_consent(self):
        participants_consent = self.cleaned_data.get('participants_consent')
        if participants_consent not in ['yes', 'no']:
            raise forms.ValidationError(_("Пожалуйста, выберите согласие на обработку персональных данных."))
        return participants_consent
    



class GuestRegistrationForm(forms.ModelForm):
    class Meta:
        model = Guest
        
        fields = ['name', 'phone', 'tg', 'guest_consent']
        
        widgets = {
            'name': forms.TextInput(attrs={'class': 'input', 'id':'start-registration', 'placeholder': _('Ваше имя')}),
            'phone': forms.TextInput(attrs={'class': 'input', 'placeholder': _('Ваш телефон')}),
            'tg': forms.TextInput(attrs={'class': 'input', 'placeholder': _('Ваш ник в Телеграм')}),
            'guest_consent': forms.Select(attrs={'class': 'input'}),
        }
        
        labels = {
            'name': _('Полное имя'),
            'phone': _('Номер телефона'),
            'tg': _('Телеграм ник'),
            'guest_consent': _('Согласны ли вы на обработку персональных данных?'),
        }

    
    def clean_name(self):
        name = self.cleaned_data.get('name')
        if not name or not str(name).strip():
            raise forms.ValidationError(_("Полное имя обязательно."))
        return str(name).strip()
    
    def clean_phone(self):
        phone = self.cleaned_data.get('phone')
        if not phone or not str(phone).strip():
            raise forms.ValidationError(_("Номер телефона обязателен."))
        return str(phone).strip()
    
    def clean_tg(self):
        tg = self.cleaned_data.get('tg')
        if not tg or not str(tg).strip():
            raise forms.ValidationError(_("Телеграм ник обязателен."))
        return str(tg).strip()

    def clean_guest_consent(self):
        guest_consent = self.cleaned_data.get('guest_consent')
        if guest_consent not in ['yes', 'no']:
            raise forms.ValidationError(_("Пожалуйста, выберите согласие на обработку персональных данных."))
        return guest_consent