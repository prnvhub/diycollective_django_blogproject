# Generated by Django 3.2.6 on 2021-11-21 06:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0002_auto_20211121_0623'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='topic',
        ),
    ]
