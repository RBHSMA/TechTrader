# Generated by Django 3.1.6 on 2021-02-02 02:54

from django.db import migrations
import jsonfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('strategie', '0003_auto_20210129_2044'),
    ]

    operations = [
        migrations.AlterField(
            model_name='strategie',
            name='regeln',
            field=jsonfield.fields.JSONField(default=dict),
        ),
    ]
