# Generated by Django 3.0.6 on 2020-05-14 18:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('savingsapp', '0009_auto_20200514_2104'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendance',
            name='status',
            field=models.BooleanField(default=False),
        ),
    ]
