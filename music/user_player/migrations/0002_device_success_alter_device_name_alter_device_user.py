# Generated by Django 4.1.7 on 2023-04-18 00:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_player', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='device',
            name='success',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='device',
            name='name',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='device',
            name='user',
            field=models.CharField(max_length=40),
        ),
    ]
