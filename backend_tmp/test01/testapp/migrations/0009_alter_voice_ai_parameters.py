# Generated by Django 5.0.6 on 2024-05-31 09:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0008_daily_intake_info_medication'),
    ]

    operations = [
        migrations.AlterField(
            model_name='voice_ai',
            name='parameters',
            field=models.FileField(upload_to='uploads/'),
        ),
    ]