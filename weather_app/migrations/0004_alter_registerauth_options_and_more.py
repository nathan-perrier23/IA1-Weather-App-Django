# Generated by Django 4.1.2 on 2024-01-07 08:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('weather_app', '0003_registerauth'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='registerauth',
            options={},
        ),
        migrations.RemoveField(
            model_name='registerauth',
            name='date_joined',
        ),
        migrations.RemoveField(
            model_name='registerauth',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='registerauth',
            name='groups',
        ),
        migrations.RemoveField(
            model_name='registerauth',
            name='is_active',
        ),
        migrations.RemoveField(
            model_name='registerauth',
            name='is_staff',
        ),
        migrations.RemoveField(
            model_name='registerauth',
            name='is_superuser',
        ),
        migrations.RemoveField(
            model_name='registerauth',
            name='last_login',
        ),
        migrations.RemoveField(
            model_name='registerauth',
            name='last_name',
        ),
        migrations.RemoveField(
            model_name='registerauth',
            name='password',
        ),
        migrations.RemoveField(
            model_name='registerauth',
            name='user_permissions',
        ),
        migrations.RemoveField(
            model_name='registerauth',
            name='username',
        ),
    ]
