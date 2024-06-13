# Generated by Django 5.0.6 on 2024-06-11 23:55

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('eventos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Participant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('phone_number', models.CharField(max_length=15)),
                ('document_id', models.CharField(max_length=100, unique=True)),
                ('status', models.BooleanField(default=True)),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='eventos.event')),
            ],
        ),
    ]
