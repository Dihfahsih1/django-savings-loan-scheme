# Generated by Django 3.0.6 on 2020-05-13 19:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('savingsapp', '0002_auto_20200513_2208'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cycle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cycle_name', models.CharField(blank=True, max_length=220, null=True, unique=True)),
                ('rate', models.IntegerField(default=15)),
                ('cycle_period_start', models.DateField(max_length=255, unique=True)),
                ('cycle_period_end', models.DateField(max_length=255, unique=True)),
                ('is_active', models.BooleanField(default=True)),
            ],
        ),
        migrations.AlterField(
            model_name='saving',
            name='cycle',
            field=models.ForeignKey(blank=True, max_length=100, null=True, on_delete=django.db.models.deletion.SET_NULL, to='savingsapp.Cycle'),
        ),
    ]
