# Generated by Django 3.2 on 2021-04-14 15:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bot', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Members',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_t', models.CharField(max_length=60, verbose_name='Телеграм ID')),
                ('name', models.CharField(max_length=110, verbose_name='ИМЯ')),
            ],
            options={
                'verbose_name': 'Подписчика',
                'verbose_name_plural': 'Подписчики',
            },
        ),
    ]