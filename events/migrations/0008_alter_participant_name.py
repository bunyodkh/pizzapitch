# Generated by Django 5.2.4 on 2025-07-24 16:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0007_alter_participant_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='participant',
            name='name',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Имя'),
        ),
    ]
