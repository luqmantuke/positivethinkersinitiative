# Generated by Django 3.1.4 on 2021-03-19 14:35

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('career', '0002_auto_20210319_1403'),
    ]

    operations = [
        migrations.AlterField(
            model_name='career',
            name='date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
