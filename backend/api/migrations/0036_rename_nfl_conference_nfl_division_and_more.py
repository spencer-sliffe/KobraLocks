# Generated by Django 4.2.11 on 2024-06-27 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0035_nflplayertotals_under_american_odds_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='NFL_Conference',
            new_name='NFL_Division',
        ),
        migrations.RenameField(
            model_name='nfl_division',
            old_name='CID',
            new_name='DID',
        ),
        migrations.RenameField(
            model_name='nfl_division',
            old_name='CYID',
            new_name='DYID',
        ),
        migrations.RenameField(
            model_name='nfl_player',
            old_name='CYID',
            new_name='DYID',
        ),
        migrations.RenameField(
            model_name='nfl_team',
            old_name='CYID',
            new_name='DYID',
        ),
        migrations.RenameField(
            model_name='nfl_team',
            old_name='conference_standing',
            new_name='division_standing',
        ),
    ]
