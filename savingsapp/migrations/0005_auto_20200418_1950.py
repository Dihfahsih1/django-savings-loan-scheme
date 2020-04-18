# Generated by Django 2.2.8 on 2020-04-18 16:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('savingsapp', '0004_auto_20200418_1801'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='date',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='customuser',
            name='social_fund',
            field=models.IntegerField(blank=True, default=1000, null=True),
        ),
        migrations.AddField(
            model_name='customuser',
            name='status',
            field=models.CharField(blank=True, choices=[('Present', 'Present'), ('Absent', 'Absent')], default='Present', max_length=123, null=True),
        ),
        migrations.DeleteModel(
            name='Attendance',
        ),
    ]
