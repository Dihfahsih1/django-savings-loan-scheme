# Generated by Django 2.2.8 on 2020-04-19 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('savingsapp', '0009_lookups'),
    ]

    operations = [
        migrations.CreateModel(
            name='LookupsDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('details', models.CharField(max_length=255)),
            ],
        ),
        migrations.RemoveField(
            model_name='lookups',
            name='lookup_id',
        ),
    ]