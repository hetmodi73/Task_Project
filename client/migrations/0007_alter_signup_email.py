# Generated by Django 4.0 on 2022-04-08 13:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0006_signup'),
    ]

    operations = [
        migrations.AlterField(
            model_name='signup',
            name='email',
            field=models.CharField(max_length=30),
        ),
    ]
