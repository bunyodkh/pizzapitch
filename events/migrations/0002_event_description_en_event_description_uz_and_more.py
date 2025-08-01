# Generated by Django 5.2.4 on 2025-07-24 08:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='description_en',
            field=models.TextField(blank=True, null=True, verbose_name='Описание на английском'),
        ),
        migrations.AddField(
            model_name='event',
            name='description_uz',
            field=models.TextField(blank=True, null=True, verbose_name='Описание на узбекском'),
        ),
        migrations.AddField(
            model_name='event',
            name='location_en',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Место проведения на английском'),
        ),
        migrations.AddField(
            model_name='event',
            name='location_uz',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Место проведения на узбекском'),
        ),
        migrations.AddField(
            model_name='eventtype',
            name='description_en',
            field=models.TextField(blank=True, null=True, verbose_name='Описание на английском'),
        ),
        migrations.AddField(
            model_name='eventtype',
            name='description_uz',
            field=models.TextField(blank=True, null=True, verbose_name='Описание на узбекском'),
        ),
        migrations.AddField(
            model_name='eventtype',
            name='title_code',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Код названия'),
        ),
        migrations.AddField(
            model_name='participant',
            name='selected',
            field=models.BooleanField(default=False, verbose_name='Выбран'),
        ),
        migrations.AlterField(
            model_name='event',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='events/', verbose_name='Изображение'),
        ),
    ]
