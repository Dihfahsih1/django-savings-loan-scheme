# Generated by Django 3.0.6 on 2020-05-17 09:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('savingsapp', '0017_auto_20200515_1159'),
    ]

    operations = [
        migrations.AddField(
            model_name='cycle',
            name='active',
            field=models.BooleanField(default=False),
        ),
    ]
