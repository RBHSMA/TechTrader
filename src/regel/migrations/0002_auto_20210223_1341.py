# Generated by Django 3.1.6 on 2021-02-23 13:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('regel', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='regel',
            old_name='code',
            new_name='berechnung_pseudo_code',
        ),
    ]
