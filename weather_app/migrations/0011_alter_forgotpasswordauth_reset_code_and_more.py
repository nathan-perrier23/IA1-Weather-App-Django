# Generated by Django 4.1.2 on 2024-01-27 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('weather_app', '0010_alter_customuser_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='forgotpasswordauth',
            name='reset_code',
            field=models.CharField(max_length=256),
        ),
        migrations.AlterField(
            model_name='registerauth',
            name='reset_code',
            field=models.CharField(max_length=256),
        ),
    ]
