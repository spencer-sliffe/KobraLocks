# Generated by Django 4.2.11 on 2024-06-21 18:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0031_nflplayertotals_under_american_odds'),
    ]

    operations = [
        migrations.AddField(
            model_name='mlb_player',
            name='caught_stealing',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
