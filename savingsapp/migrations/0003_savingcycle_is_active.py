# Generated by Django 2.2.8 on 2020-04-29 16:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('savingsapp', '0002_auto_20200429_1334'),
    ]

    operations = [
        migrations.AddField(
            model_name='savingcycle',
            name='is_active',
            field=models.BooleanField(blank=True, default=True, null=True),
        ),
    ]
