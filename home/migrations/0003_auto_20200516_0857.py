# Generated by Django 3.0.2 on 2020-05-16 15:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_auto_20200516_0853'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='timestamp',
            new_name='timeStamp',
        ),
    ]
