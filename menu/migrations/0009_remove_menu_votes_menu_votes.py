# Generated by Django 4.0.6 on 2022-07-17 16:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0008_alter_vote_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='menu',
            name='votes',
        ),
        migrations.AddField(
            model_name='menu',
            name='votes',
            field=models.ManyToManyField(to='menu.vote'),
        ),
    ]
