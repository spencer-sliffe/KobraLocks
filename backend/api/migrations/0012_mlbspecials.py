# Generated by Django 4.2.11 on 2024-06-12 16:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0011_mlbfutures'),
    ]

    operations = [
        migrations.CreateModel(
            name='MLBSpecials',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('section_title', models.CharField(max_length=100)),
                ('bet_titles', models.JSONField()),
                ('odds', models.JSONField()),
            ],
        ),
    ]