# Generated by Django 3.1.6 on 2021-03-15 10:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('simulation', '0007_auto_20210310_2046'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='simulation',
            name='nutzername',
        ),
    ]