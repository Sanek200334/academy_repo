# Generated by Django 2.2.4 on 2020-05-10 11:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0002_customuser_phone'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='ads',
        ),
        migrations.AddField(
            model_name='ad',
            name='owner',
            field=models.CharField(default='', max_length=255),
        ),
    ]
