# Generated by Django 3.1.4 on 2021-03-17 14:28

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Career',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=1000)),
                ('image', models.ImageField(null=True, upload_to='our_impacts')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('description', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('position', models.CharField(max_length=3000)),
                ('slug', models.SlugField(blank=True, null=True)),
            ],
        ),
    ]
