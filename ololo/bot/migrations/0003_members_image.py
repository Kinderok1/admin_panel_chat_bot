# Generated by Django 3.2 on 2021-04-14 15:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bot', '0002_members'),
    ]

    operations = [
        migrations.AddField(
            model_name='members',
            name='image',
            field=models.ImageField(null=True, upload_to='avatars'),
        ),
    ]
