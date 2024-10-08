# Generated by Django 4.2.16 on 2024-09-15 02:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cv', '0003_education_major'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='education',
            name='votes',
        ),
        migrations.RemoveField(
            model_name='skills',
            name='votes',
        ),
        migrations.RemoveField(
            model_name='work_experience',
            name='votes',
        ),
        migrations.AlterField(
            model_name='education',
            name='study_from',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='education',
            name='study_to',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='work_experience',
            name='work_from',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='work_experience',
            name='work_to',
            field=models.CharField(max_length=100),
        ),
    ]
