# Generated by Django 3.0.6 on 2020-05-15 08:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('savingsapp', '0016_auto_20200515_1151'),
    ]

    operations = [
        migrations.AlterField(
            model_name='socialfund',
            name='full_name',
            field=models.CharField(blank=True, max_length=220, null=True),
        ),
    ]
