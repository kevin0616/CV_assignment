# Generated by Django 4.2.16 on 2024-09-13 21:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cv', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='education',
            old_name='name',
            new_name='personal_info',
        ),
        migrations.RenameField(
            model_name='skills',
            old_name='name',
            new_name='personal_info',
        ),
        migrations.RenameField(
            model_name='work_experience',
            old_name='name',
            new_name='personal_info',
        ),
    ]
