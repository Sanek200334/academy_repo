# Generated by Django 3.0.5 on 2020-05-16 10:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0004_customuser_avatar'),
    ]

    operations = [
        migrations.AddField(
            model_name='ad',
            name='owner_id',
            field=models.IntegerField(default=0),
        ),
    ]
