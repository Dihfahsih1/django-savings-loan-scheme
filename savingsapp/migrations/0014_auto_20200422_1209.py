# Generated by Django 2.2.8 on 2020-04-22 09:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('savingsapp', '0013_auto_20200421_1338'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendance',
            name='full_name',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]