# Generated by Django 3.0.8 on 2020-08-19 19:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_auto_20200722_2046'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='user',
            new_name='writer',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='user',
            new_name='writer',
        ),
    ]
