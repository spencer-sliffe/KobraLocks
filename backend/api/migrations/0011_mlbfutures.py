# Generated by Django 4.2.11 on 2024-06-12 15:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0010_alter_mlbgame_game_time_alter_mlsgame_game_time_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='MLBFutures',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('section_title', models.CharField(max_length=100)),
                ('teams', models.TextField()),
                ('odds', models.TextField()),
            ],
        ),
    ]