# Generated by Django 3.0.5 on 2020-05-23 14:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0007_auto_20200523_1414'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='feedback',
            name='subject',
        ),
        migrations.RemoveField(
            model_name='feedback',
            name='text',
        ),
    ]
