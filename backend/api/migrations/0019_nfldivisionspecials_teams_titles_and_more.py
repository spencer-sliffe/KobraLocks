# Generated by Django 4.2.11 on 2024-06-13 17:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0018_ncaabbfutures_nfldivisionspecials_nflfutures_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='NFLDivisionSpecials',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('section_title', models.CharField(max_length=100)),
                ('bet_titles', models.TextField(null=True)),
                ('team_titles', models.TextField(null=True)),
                ('odds', models.TextField()),
            ],
        ),
    ]