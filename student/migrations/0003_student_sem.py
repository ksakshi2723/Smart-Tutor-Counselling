# Generated by Django 3.0.4 on 2020-04-28 19:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0002_remove_student_sem'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='sem',
            field=models.CharField(choices=[('1', 'I'), ('2', 'II'), ('3', 'III'), ('4', 'IV'), ('5', 'V'), ('6', 'VI'), ('7', 'VII'), ('8', 'VIII')], default='I', max_length=2),
        ),
    ]
