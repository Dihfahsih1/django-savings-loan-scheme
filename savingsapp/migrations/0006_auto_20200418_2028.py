# Generated by Django 2.2.8 on 2020-04-18 17:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('savingsapp', '0005_auto_20200418_1950'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='attendance_month',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='customuser',
            name='attendance_year',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
