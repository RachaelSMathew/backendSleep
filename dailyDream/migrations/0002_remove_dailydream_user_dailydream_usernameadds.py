# Generated by Django 5.0 on 2023-12-19 23:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dailyDream', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dailydream',
            name='user',
        ),
        migrations.AddField(
            model_name='dailydream',
            name='userNameAddS',
            field=models.CharField(default='null', max_length=100),
            preserve_default=False,
        ),
    ]
