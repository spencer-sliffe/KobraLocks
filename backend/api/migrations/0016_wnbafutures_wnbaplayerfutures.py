# Generated by Django 4.2.11 on 2024-06-12 19:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0015_nbafutures_nbaplayerfutures'),
    ]

    operations = [
        migrations.CreateModel(
            name='WNBAFutures',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('section_title', models.CharField(max_length=100)),
                ('teams', models.TextField()),
                ('odds', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='WNBAPlayerFutures',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('section_title', models.CharField(max_length=100)),
                ('players', models.TextField()),
                ('odds', models.TextField()),
            ],
        ),
    ]