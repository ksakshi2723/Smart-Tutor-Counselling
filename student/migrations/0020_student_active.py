# Generated by Django 3.0.6 on 2020-09-17 09:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0019_attendance_week'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='active',
            field=models.BooleanField(default=True),
        ),
    ]