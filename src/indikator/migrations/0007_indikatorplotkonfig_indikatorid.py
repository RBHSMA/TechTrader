# Generated by Django 3.1.6 on 2021-03-29 13:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('indikator', '0006_indikatorplotkonfig'),
    ]

    operations = [
        migrations.AddField(
            model_name='indikatorplotkonfig',
            name='indikatorId',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
