from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils import timezone


class EventType(models.Model):
    title = models.CharField(max_length=200, verbose_name=_("Название"))
    title_code = models.CharField(max_length=50, verbose_name=_("Код названия"), blank=True, null=True)
    
    description = models.TextField(verbose_name=_("Описание"), blank=True, null=True)
    description_uz = models.TextField(verbose_name=_("Описание на узбекском"), blank=True, null=True)
    description_en = models.TextField(verbose_name=_("Описание на английском"), blank=True, null=True)
    
    image = models.ImageField(upload_to='events/', verbose_name=_("Изображение"), null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("Дата создания"))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_("Дата обновления"))

    class Meta:
        verbose_name = _("Тип мероприятия")
        verbose_name_plural = _("Типы мероприятий")

    def __str__(self):
        return self.title


class Event(models.Model):
    event_type = models.ForeignKey(EventType, on_delete=models.CASCADE, verbose_name=_("Тип мероприятия"))
    
    title = models.CharField(max_length=200, verbose_name=_("Название"))
    title_spot = models.CharField(max_length=200, verbose_name=_("Акцент к названию"))


    description = models.TextField(verbose_name=_("Описание"))
    description_uz = models.TextField(verbose_name=_("Описание на узбекском"), blank=True, null=True)
    description_en = models.TextField(verbose_name=_("Описание на английском"), blank=True, null=True)

    image = models.ImageField(upload_to='events/', verbose_name=_("Изображение"), null=True, blank=True)
    
    date = models.DateTimeField(verbose_name=_("Дата и время"))
    
    location = models.CharField(max_length=200, verbose_name=_("Место проведения"))
    location_uz = models.CharField(max_length=200, verbose_name=_("Место проведения на узбекском"), blank=True, null=True)
    location_en = models.CharField(max_length=200, verbose_name=_("Место проведения на английском"), blank=True, null=True)
    

    registration_deadline = models.DateTimeField(verbose_name=_("Крайний срок регистрации"))
    is_active = models.BooleanField(default=True, verbose_name=_("Активно"))
    registration_closed = models.BooleanField(default=False, verbose_name=_("Регистрация закрыта"))

    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("Дата создания"))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_("Дата обновления"))

    class Meta:
        verbose_name = _("Мероприятие")
        verbose_name_plural = _("Мероприятия")

    def __str__(self):
        return f'{self.title}{self.title_spot}'
    
    def save(self, *args, **kwargs):
        if self.registration_deadline and self.registration_deadline < timezone.now():
            self.registration_closed = True  
        if self.is_active:
            Event.objects.exclude(pk=self.pk).filter(is_active=True).update(is_active=False)
        super().save(*args, **kwargs)
    


class Participant(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE, verbose_name=_("Мероприятие"))
    
    name = models.CharField(max_length=200, verbose_name=_("Имя"), blank=True, null=True)
    phone = models.CharField(max_length=15, verbose_name=_("Телефон"), blank=True, null=True)
    tg = models.CharField(max_length=15, verbose_name=_("Телеграм"), blank=True, null=True)
    
    startup = models.CharField(max_length=200, verbose_name=_("Название стартапа"), blank=True, null=True)
    startup_description = models.TextField(verbose_name=_("Описание стартапа"), blank=True, null=True)
    presentation_link = models.CharField(max_length=500, verbose_name=_("Ссылка на презентацию"), blank=True, null=True)

    CONSENT_CHOICES = [
        ('yes', _("Да")),
        ('no', _("Нет")),
    ]

    consent = models.CharField(
        max_length=5,
        choices=CONSENT_CHOICES,
        default='no',
        verbose_name=_("Согласие на обработку персональных данных")
    )

    selected = models.BooleanField(default=False, verbose_name=_("Выбран"))

    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("Дата создания"))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_("Дата обновления"))


    class Meta:
        verbose_name = _("Участник")
        verbose_name_plural = _("Участники")

    def __str__(self):
        return self.name