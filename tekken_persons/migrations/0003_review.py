# Generated by Django 3.2.5 on 2024-01-23 11:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tekken_persons', '0002_auto_20240123_1310'),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('tekken_person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tekken_reviews', to='tekken_persons.personsgame')),
            ],
        ),
    ]