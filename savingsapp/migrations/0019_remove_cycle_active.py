# Generated by Django 3.0.6 on 2020-05-17 10:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('savingsapp', '0018_cycle_active'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cycle',
            name='active',
        ),
    ]
