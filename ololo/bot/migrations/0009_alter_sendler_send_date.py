# Generated by Django 3.2 on 2021-04-16 14:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bot', '0008_alter_sendler_send_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sendler',
            name='send_date',
            field=models.DateTimeField(null=True),
        ),
    ]
