# Generated by Django 3.0.6 on 2020-05-24 12:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('savingsapp', '0024_auto_20200524_1511'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='joining_date',
            field=models.DateTimeField(auto_now_add=True, default='2020-10-10'),
            preserve_default=False,
        ),
    ]
