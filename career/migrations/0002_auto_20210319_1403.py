# Generated by Django 3.1.4 on 2021-03-19 14:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('career', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='career',
            name='image',
            field=models.ImageField(null=True, upload_to='career'),
        ),
    ]