# Generated by Django 4.1.10 on 2023-07-20 09:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='registration',
            old_name='first_name',
            new_name='fullname',
        ),
        migrations.RenameField(
            model_name='registration',
            old_name='last_name',
            new_name='phone_no',
        ),
    ]
