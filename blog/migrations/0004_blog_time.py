# Generated by Django 4.1 on 2022-08-25 08:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_alter_blog_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='time',
            field=models.TimeField(null=True),
        ),
    ]
