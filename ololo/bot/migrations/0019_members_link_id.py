# Generated by Django 3.2 on 2021-05-14 14:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bot', '0018_alter_items_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='members',
            name='link_id',
            field=models.CharField(blank=True, max_length=300, null=True, verbose_name='Ссылка телеграм'),
        ),
    ]