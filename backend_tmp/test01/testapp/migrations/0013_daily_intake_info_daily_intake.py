# Generated by Django 5.0.6 on 2024-06-05 07:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0012_hospital_history_duration'),
    ]

    operations = [
        migrations.AddField(
            model_name='daily_intake_info',
            name='daily_intake',
            field=models.PositiveIntegerField(default=3),
        ),
    ]