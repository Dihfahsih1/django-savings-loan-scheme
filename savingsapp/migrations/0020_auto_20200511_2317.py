# Generated by Django 3.0.5 on 2020-05-11 20:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('savingsapp', '0019_auto_20200505_1846'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='loan',
            name='is_loanee',
        ),
        migrations.AddField(
            model_name='loan',
            name='loan_status',
            field=models.CharField(choices=[('RUNNING', 'RUNNING'), ('SETTLED', 'SETTLED')], default='RUNNING', max_length=100),
        ),
    ]
