# Generated by Django 3.2 on 2021-04-21 12:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bot', '0010_auto_20210416_1822'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sendler',
            name='status',
            field=models.CharField(max_length=35, null=True, verbose_name='Статус'),
        ),
        migrations.CreateModel(
            name='Notifications',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_read', models.BooleanField(default=False)),
                ('url_to_dialog', models.CharField(blank=True, max_length=50, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('from_user_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='bot.members')),
            ],
            options={
                'ordering': ['-created_at'],
            },
        ),
    ]
