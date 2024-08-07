# Generated by Django 4.2.11 on 2024-06-20 18:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0029_nflplayertotals_under_american_odds_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='mlb_player',
            name='at_bats',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='mlb_player',
            name='batting_average',
            field=models.DecimalField(blank=True, decimal_places=3, max_digits=5, null=True),
        ),
        migrations.AddField(
            model_name='mlb_player',
            name='batting_average_against',
            field=models.DecimalField(blank=True, decimal_places=3, max_digits=5, null=True),
        ),
        migrations.AddField(
            model_name='mlb_player',
            name='complete_games',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='mlb_player',
            name='double_plays',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='mlb_player',
            name='doubles',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='mlb_player',
            name='earned_run_average',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True),
        ),
        migrations.AddField(
            model_name='mlb_player',
            name='earned_runs',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='mlb_player',
            name='errors',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='mlb_player',
            name='fielding_percentage',
            field=models.DecimalField(blank=True, decimal_places=3, max_digits=5, null=True),
        ),
        migrations.AddField(
            model_name='mlb_player',
            name='games',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='mlb_player',
            name='games_started',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='mlb_player',
            name='hits',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='mlb_player',
            name='holds',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='mlb_player',
            name='home_runs',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='mlb_player',
            name='innings_pitched',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True),
        ),
        migrations.AddField(
            model_name='mlb_player',
            name='losses',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='mlb_player',
            name='number_of_pitches',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='mlb_player',
            name='on_base_percentage',
            field=models.DecimalField(blank=True, decimal_places=3, max_digits=5, null=True),
        ),
        migrations.AddField(
            model_name='mlb_player',
            name='on_base_plus_slugging',
            field=models.DecimalField(blank=True, decimal_places=3, max_digits=5, null=True),
        ),
        migrations.AddField(
            model_name='mlb_player',
            name='p_games',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='mlb_player',
            name='p_hits',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='mlb_player',
            name='p_home_runs',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='mlb_player',
            name='p_runs',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='mlb_player',
            name='p_strike_outs',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='mlb_player',
            name='p_walks',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='mlb_player',
            name='position',
            field=models.CharField(blank=True, max_length=5, null=True),
        ),
        migrations.AddField(
            model_name='mlb_player',
            name='runs',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='mlb_player',
            name='runs_batted_in',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='mlb_player',
            name='save_opportunities',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='mlb_player',
            name='saves',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='mlb_player',
            name='shut_outs',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='mlb_player',
            name='slugging_percentage',
            field=models.DecimalField(blank=True, decimal_places=3, max_digits=5, null=True),
        ),
        migrations.AddField(
            model_name='mlb_player',
            name='stolen_bases',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='mlb_player',
            name='strike_outs',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='mlb_player',
            name='total_bases',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='mlb_player',
            name='triples',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='mlb_player',
            name='walks',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='mlb_player',
            name='whip',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True),
        ),
        migrations.AddField(
            model_name='mlb_player',
            name='wins',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='mlb_team',
            name='at_bats',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='mlb_team',
            name='batting_average',
            field=models.DecimalField(decimal_places=3, default=0, max_digits=5),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='mlb_team',
            name='batting_average_against',
            field=models.DecimalField(decimal_places=3, default=0, max_digits=5),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='mlb_team',
            name='caught_stealing',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='mlb_team',
            name='doubles',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='mlb_team',
            name='earned_run_average',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=5),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='mlb_team',
            name='earned_runs',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='mlb_team',
            name='games',
            field=models.PositiveIntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='mlb_team',
            name='hits',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='mlb_team',
            name='holds',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='mlb_team',
            name='home_runs',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='mlb_team',
            name='losses',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='mlb_team',
            name='on_base_percentage',
            field=models.DecimalField(decimal_places=3, default=0, max_digits=5),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='mlb_team',
            name='on_base_plus_slugging',
            field=models.DecimalField(decimal_places=3, default=0, max_digits=5),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='mlb_team',
            name='p_hits',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='mlb_team',
            name='p_home_runs',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='mlb_team',
            name='p_runs',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='mlb_team',
            name='p_strike_outs',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='mlb_team',
            name='p_walks',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='mlb_team',
            name='runs',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='mlb_team',
            name='runs_batted_in',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='mlb_team',
            name='save_opportunities',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='mlb_team',
            name='saves',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='mlb_team',
            name='shut_outs',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='mlb_team',
            name='slugging_percentage',
            field=models.DecimalField(decimal_places=3, default=0, max_digits=5),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='mlb_team',
            name='stolen_bases',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='mlb_team',
            name='strike_outs',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='mlb_team',
            name='triples',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='mlb_team',
            name='walks',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='mlb_team',
            name='whip',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=5),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='mlb_team',
            name='wins',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
