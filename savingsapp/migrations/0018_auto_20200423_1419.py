# Generated by Django 2.2.8 on 2020-04-23 11:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('savingsapp', '0017_auto_20200422_1615'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendance',
            name='date',
            field=models.DateField(blank=True, null=True),
        ),
    ]