# Generated by Django 4.2 on 2023-04-21 16:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booking',
            name='Book_id',
        ),
        migrations.RemoveField(
            model_name='menu',
            name='Menu_id',
        ),
    ]
