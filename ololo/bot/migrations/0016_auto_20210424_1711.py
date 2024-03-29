# Generated by Django 3.2 on 2021-04-24 14:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bot', '0015_auto_20210423_2027'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='type',
            options={'verbose_name': 'Категория', 'verbose_name_plural': 'Категории'},
        ),
        migrations.AddField(
            model_name='members',
            name='user_state',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='type',
            name='name',
            field=models.CharField(help_text='Добавьте новую категорию(например Японская кухня, Закуски и т.п)', max_length=200),
        ),
    ]
