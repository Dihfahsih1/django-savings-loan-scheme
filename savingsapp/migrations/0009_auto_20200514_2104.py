# Generated by Django 3.0.6 on 2020-05-14 18:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('savingsapp', '0008_customuser_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendance',
            name='full_name',
            field=models.CharField(blank=True, max_length=123, null=True),
        ),
    ]