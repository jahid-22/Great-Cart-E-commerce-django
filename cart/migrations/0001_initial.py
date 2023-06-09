# Generated by Django 4.1.6 on 2023-06-01 15:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Catagory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('catagory_name', models.CharField(max_length=40, unique=True)),
                ('slug', models.SlugField(max_length=200, unique=True)),
                ('description', models.TextField(blank=True, max_length=300)),
                ('img', models.ImageField(blank=True, upload_to='projectImg')),
            ],
            options={
                'verbose_name': 'catagory',
                'verbose_name_plural': 'catagories',
            },
        ),
    ]
