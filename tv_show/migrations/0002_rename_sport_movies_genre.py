# Generated by Django 3.2.5 on 2024-01-23 17:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tv_show', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='movies',
            old_name='sport',
            new_name='genre',
        ),
    ]
