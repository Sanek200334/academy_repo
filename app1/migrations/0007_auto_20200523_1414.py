# Generated by Django 3.0.5 on 2020-05-23 14:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0006_feedback'),
    ]

    operations = [
        migrations.AddField(
            model_name='feedback',
            name='whom',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AddField(
            model_name='feedback',
            name='whose',
            field=models.CharField(default='', max_length=255),
        ),
    ]
