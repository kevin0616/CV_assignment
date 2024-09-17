# Generated by Django 4.2.16 on 2024-09-13 21:22

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Personal_info',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('phone_number', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('website', models.CharField(max_length=100)),
                ('city_live_in', models.CharField(max_length=100)),
                ('country_live_in', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Work_experience',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=100)),
                ('job_title', models.CharField(max_length=100)),
                ('job_description', models.CharField(max_length=300)),
                ('work_from', models.DateField(default=datetime.date.today)),
                ('work_to', models.DateField(default=datetime.date.today)),
                ('city_in', models.CharField(max_length=100)),
                ('country_in', models.CharField(max_length=100)),
                ('votes', models.IntegerField(default=0)),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cv.personal_info')),
            ],
        ),
        migrations.CreateModel(
            name='Skills',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('skill_name', models.CharField(max_length=100)),
                ('skill_description', models.CharField(max_length=300)),
                ('votes', models.IntegerField(default=0)),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cv.personal_info')),
            ],
        ),
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('school_name', models.CharField(max_length=100)),
                ('degree', models.CharField(max_length=100)),
                ('study_from', models.DateField(default=datetime.date.today)),
                ('study_to', models.DateField(default=datetime.date.today)),
                ('city_in', models.CharField(max_length=100)),
                ('country_in', models.CharField(max_length=100)),
                ('votes', models.IntegerField(default=0)),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cv.personal_info')),
            ],
        ),
    ]
