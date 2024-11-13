# Generated by Django 5.1.2 on 2024-11-13 03:06

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('dashboard', '0005_alter_educationprofile_qualifications'),
    ]

    operations = [
        migrations.CreateModel(
            name='OTP',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('otp', models.CharField(blank=True, max_length=6, null=True)),
                ('otp_created_at', models.DateTimeField(blank=True, null=True)),
            ],
        ),
    ]
