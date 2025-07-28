from django.db import models
from PIL import Image
from django.utils.translation import gettext_lazy as _

class Partner(models.Model):
    name = models.CharField(max_length=100, verbose_name=_("Название партнера"), help_text=_("Введите название партнера"))
    image = models.ImageField(upload_to='partners/', verbose_name=_("Логотип"), null=False, blank=False, help_text=_("Загрузите логотип партнера"))
    website = models.URLField(verbose_name=_("Веб-сайт"), null=True, blank=True, help_text=_("Введите URL веб-сайта партнера"))

    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("Создано"))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_("Обновлено"))

    show = models.BooleanField(default=True, verbose_name=_("Показывать на сайте"), help_text=_("Отметьте, если хотите показать партнера на сайте"))

    class Meta:
        verbose_name = _("Партнер")
        verbose_name_plural = _("Партнеры")
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
