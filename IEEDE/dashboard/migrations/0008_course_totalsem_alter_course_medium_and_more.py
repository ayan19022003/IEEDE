# Generated by Django 5.1.2 on 2024-11-13 19:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0007_remove_educationprofile_department_course_department'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='totalsem',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='medium',
            field=models.CharField(choices=[('online', 'Online'), ('offline', 'Offline')], default='offline', max_length=7),
        ),
        migrations.AlterField(
            model_name='course',
            name='type',
            field=models.CharField(choices=[('deg', 'Degree'), ('cert', 'Certificates')], default='deg', max_length=4),
        ),
    ]
