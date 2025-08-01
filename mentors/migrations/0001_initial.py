# Generated by Django 5.2.4 on 2025-07-27 17:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Mentor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Введите полное имя ментора', max_length=100, verbose_name='Имя')),
                ('email', models.EmailField(blank=True, help_text='Введите электронную почту ментора', max_length=254, null=True, unique=True, verbose_name='Электронная почта')),
                ('phone', models.CharField(blank=True, help_text='Введите номер телефона ментора', max_length=15, null=True, verbose_name='Телефон')),
                ('position', models.TextField(blank=True, help_text='Укажите должность или роль ментора', null=True, verbose_name='Должность')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Создано')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Обновлено')),
            ],
            options={
                'verbose_name': 'Ментор',
                'verbose_name_plural': 'Менторы',
                'ordering': ['name'],
            },
        ),
    ]
