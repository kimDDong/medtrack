# Generated by Django 5.0.6 on 2024-05-22 08:02

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='medication_info',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('medication', models.CharField(max_length=100)),
                ('manual_addition', models.BooleanField(default=False)),
                ('daily_intake', models.PositiveIntegerField()),
                ('added_date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='user_personal_info',
            fields=[
                ('social_number', models.CharField(max_length=14, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=100)),
                ('user_id', models.CharField(max_length=20)),
                ('password', models.CharField(max_length=20)),
                ('phone_number', models.CharField(max_length=13)),
                ('address', models.CharField(max_length=100)),
                ('preferred_hospital', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='daily_intake_info',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('actual_intake', models.PositiveIntegerField()),
                ('medication_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='testapp.medication_info')),
            ],
        ),
        migrations.AddField(
            model_name='medication_info',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='testapp.user_personal_info'),
        ),
    ]
