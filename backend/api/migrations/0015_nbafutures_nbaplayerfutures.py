# Generated by Django 4.2.11 on 2024-06-12 18:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0014_mlbplayerfutures_mlbteamplayoffs_mlbwintotals'),
    ]

    operations = [
        migrations.CreateModel(
            name='NBAFutures',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('section_title', models.CharField(max_length=100)),
                ('teams', models.TextField()),
                ('odds', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='NBAPlayerFutures',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('section_title', models.CharField(max_length=100)),
                ('players', models.TextField()),
                ('odds', models.TextField()),
            ],
        ),
    ]
