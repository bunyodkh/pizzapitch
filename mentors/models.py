from django.db import models
from django.utils.translation import gettext_lazy as _
from PIL import Image

class Mentor(models.Model):   
    name = models.CharField(max_length=100, verbose_name=_("Имя"), help_text=_("Введите полное имя ментора"))
    name_uz = models.CharField(max_length=100, verbose_name=_("Имя на узбекском"), blank=True, null=True, help_text=_("Введите имя ментора на узбекском"))
    name_en = models.CharField(max_length=100, verbose_name=_("Имя на английском"), blank=True, null=True, help_text=_("Введите имя ментора на английском"))
   
    email = models.EmailField(unique=True, verbose_name=_("Электронная почта"), null=True, blank=True, help_text=_("Введите электронную почту ментора"))
    phone = models.CharField(max_length=15, verbose_name=_("Телефон"), null=True, blank=True, help_text=_("Введите номер телефона ментора"))
    
    position = models.CharField(verbose_name=_("Должность"), help_text=_("Укажите должность или роль ментора"), null=True, blank=True)
    position_uz = models.CharField(max_length=100, verbose_name=_("Должность на узбекском"), blank=True, null=True, help_text=_("Введите должность ментора на узбекском"))
    position_en = models.CharField(max_length=100, verbose_name=_("Должность на английском"), blank=True, null=True, help_text=_("Введите должность ментора на английском"))

    image = models.ImageField(upload_to='mentors/', verbose_name=_("Изображение"), null=True, blank=True, help_text=_("Загрузите изображение ментора"))

    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("Создано"))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_("Обновлено"))

    show = models.BooleanField(default=True, verbose_name=_("Показывать на сайте"), help_text=_("Отметьте, если хотите показать ментора на сайте"))

    class Meta:
        verbose_name = _("Ментор")
        verbose_name_plural = _("Менторы")
        ordering = ['name']

    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if self.image:
            img_path = self.image.path
            img = Image.open(img_path)
            max_size = (800, 800)  # Set max size (change as needed)
            img.thumbnail(max_size, Image.Resampling.LANCZOS)
            img.save(img_path, optimize=True, quality=80)  # Compress and save
