# Generated by Django 3.0.2 on 2020-05-16 15:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_auto_20200516_0857'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='timeStamp',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]