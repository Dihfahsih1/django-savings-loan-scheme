# Generated by Django 2.2.8 on 2020-04-18 10:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('savingsapp', '0002_auto_20200418_1314'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='application_fee',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]