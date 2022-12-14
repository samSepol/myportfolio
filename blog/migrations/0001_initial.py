# Generated by Django 4.1 on 2022-08-26 17:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('logo', models.ImageField(upload_to='blog_images/')),
                ('description', models.TextField()),
                ('author', models.CharField(max_length=255)),
                ('date', models.DateField()),
                ('time', models.TimeField()),
            ],
        ),
    ]
