# Generated by Django 3.0.6 on 2020-05-11 19:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('basic_rest_api', '0002_auto_20200511_1809'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='first_name',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='userprofile',
            old_name='address',
            new_name='password',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='last_name',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='website',
        ),
    ]
