# Generated by Django 3.2.6 on 2022-06-02 19:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scraping', '0008_auto_20220603_0006'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='resume',
            name='city',
        ),
        migrations.RemoveField(
            model_name='resume',
            name='language',
        ),
    ]
