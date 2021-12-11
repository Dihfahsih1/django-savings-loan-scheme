# Generated by Django 3.0.6 on 2020-05-14 08:22

from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('email', models.EmailField(blank=True, max_length=255, null=True, unique=True)),
                ('telephone', models.IntegerField(blank=True, default=0, null=True)),
                ('first_name', models.CharField(blank=True, max_length=30, null=True)),
                ('last_name', models.CharField(blank=True, max_length=255, null=True)),
                ('username', models.CharField(blank=True, max_length=30, null=True, unique=True)),
                ('application_fee', models.IntegerField(blank=True, default=10000, null=True)),
                ('Role', models.CharField(choices=[('Admin', 'Admin'), ('Ordinary', 'Ordinary')], max_length=250)),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_superuser', models.BooleanField(default=False)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Attendance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(blank=True, max_length=123, null=True)),
                ('date', models.DateField(blank=True, null=True)),
                ('status', models.BooleanField(blank=True, default=False)),
                ('social_fund', models.IntegerField(blank=True, default=0, null=True)),
                ('attendance_year', models.CharField(blank=True, default=2020, max_length=255, null=True)),
                ('attendance_month', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Cycle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cycle_name', models.CharField(blank=True, max_length=220, null=True, unique=True)),
                ('rate', models.IntegerField(blank=True, default=15, null=True)),
                ('cycle_period_start', models.DateField(max_length=255, unique=True)),
                ('cycle_period_end', models.DateField(max_length=255, unique=True)),
                ('is_active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='LookUp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=220, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='PayingLoan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('loan_id', models.CharField(blank=True, max_length=100, null=True)),
                ('date', models.DateField(blank=True, max_length=100, null=True)),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('amount', models.IntegerField(blank=True, default=0, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Stock',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ticker', models.CharField(max_length=10)),
                ('openn', models.FloatField()),
                ('close', models.FloatField()),
                ('volume', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Saving',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(blank=True, max_length=100, null=True)),
                ('amount', models.IntegerField(default=0)),
                ('cycle', models.ForeignKey(blank=True, max_length=100, null=True, on_delete=django.db.models.deletion.SET_NULL, to='savingsapp.Cycle')),
                ('name', models.ForeignKey(blank=True, max_length=100, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='LookupDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Details', models.CharField(max_length=220)),
                ('Lookup_Name', models.ForeignKey(max_length=220, on_delete=django.db.models.deletion.CASCADE, to='savingsapp.LookUp')),
            ],
        ),
        migrations.CreateModel(
            name='Loan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cycle', models.CharField(blank=True, max_length=100, null=True)),
                ('date', models.DateField(blank=True, max_length=100, null=True)),
                ('amount', models.IntegerField(default=0)),
                ('interest_rate', models.IntegerField(default=0)),
                ('loan_period', models.IntegerField(default=0)),
                ('loan_status', models.CharField(blank=True, choices=[('RUNNING', 'RUNNING'), ('SETTLED', 'SETTLED')], default='RUNNING', max_length=100, null=True)),
                ('recorded_by', models.CharField(blank=True, max_length=220, null=True)),
                ('name', models.ForeignKey(blank=True, max_length=100, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
