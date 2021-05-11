# Generated by Django 3.0.6 on 2020-10-05 17:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0023_auto_20201001_1339'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('hod', '0017_auto_20200905_0221'),
    ]

    operations = [
        migrations.CreateModel(
            name='TutorGuard',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('branch', models.CharField(choices=[('cs', 'CS'), ('it', 'IT'), ('ce', 'CE'), ('me', 'ME'), ('ec', 'EC'), ('ee', 'EE')], default='cs', max_length=10)),
                ('sem', models.CharField(choices=[('1', 'I'), ('2', 'II'), ('3', 'III'), ('4', 'IV'), ('5', 'V'), ('6', 'VI'), ('7', 'VII'), ('8', 'VIII')], default='I', max_length=2)),
                ('sec', models.CharField(choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D')], default='A', max_length=2)),
                ('teacher_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('year', models.ForeignKey(default='2017', on_delete=django.db.models.deletion.CASCADE, to='student.batch')),
            ],
            options={
                'unique_together': {('year', 'teacher_id', 'sem', 'branch', 'sec')},
            },
        ),
    ]
