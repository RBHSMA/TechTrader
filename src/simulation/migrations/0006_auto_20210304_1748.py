# Generated by Django 3.1.6 on 2021-03-04 17:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('simulation', '0005_auto_20210304_1747'),
    ]

    operations = [
        migrations.AlterField(
            model_name='simulation',
            name='isin',
            field=models.CharField(blank=True, max_length=12, null=True),
        ),
        migrations.AlterField(
            model_name='simulation',
            name='strategie',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]