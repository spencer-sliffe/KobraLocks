# Generated by Django 4.2.11 on 2024-06-28 15:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0041_nflplayertotals_under_american_odds_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='nfl_team',
            name='QB_rating',
        ),
        migrations.RemoveField(
            model_name='nfl_team',
            name='assisted_tackles',
        ),
        migrations.RemoveField(
            model_name='nfl_team',
            name='completion_percentage',
        ),
        migrations.RemoveField(
            model_name='nfl_team',
            name='extra_point_ratio',
        ),
        migrations.RemoveField(
            model_name='nfl_team',
            name='field_goal_long',
        ),
        migrations.RemoveField(
            model_name='nfl_team',
            name='field_goal_ratio',
        ),
        migrations.RemoveField(
            model_name='nfl_team',
            name='fumble_recoveries',
        ),
        migrations.RemoveField(
            model_name='nfl_team',
            name='fumble_return_yards',
        ),
        migrations.RemoveField(
            model_name='nfl_team',
            name='fumble_touchdowns',
        ),
        migrations.RemoveField(
            model_name='nfl_team',
            name='fumbles',
        ),
        migrations.RemoveField(
            model_name='nfl_team',
            name='fumbles_lost',
        ),
        migrations.RemoveField(
            model_name='nfl_team',
            name='fumbles_recovered',
        ),
        migrations.RemoveField(
            model_name='nfl_team',
            name='interception_percentage',
        ),
        migrations.RemoveField(
            model_name='nfl_team',
            name='interception_touchdowns',
        ),
        migrations.RemoveField(
            model_name='nfl_team',
            name='interception_yard_average',
        ),
        migrations.RemoveField(
            model_name='nfl_team',
            name='interceptions_caught',
        ),
        migrations.RemoveField(
            model_name='nfl_team',
            name='kick_fair_catches',
        ),
        migrations.RemoveField(
            model_name='nfl_team',
            name='kick_return_attempts',
        ),
        migrations.RemoveField(
            model_name='nfl_team',
            name='kick_return_average',
        ),
        migrations.RemoveField(
            model_name='nfl_team',
            name='kick_return_touchdowns',
        ),
        migrations.RemoveField(
            model_name='nfl_team',
            name='kick_return_yards',
        ),
        migrations.RemoveField(
            model_name='nfl_team',
            name='kicking_points',
        ),
        migrations.RemoveField(
            model_name='nfl_team',
            name='negative_yards',
        ),
        migrations.RemoveField(
            model_name='nfl_team',
            name='o_QB_rating',
        ),
        migrations.RemoveField(
            model_name='nfl_team',
            name='o_completion_percentage',
        ),
        migrations.RemoveField(
            model_name='nfl_team',
            name='o_extra_point_ratio',
        ),
        migrations.RemoveField(
            model_name='nfl_team',
            name='o_field_goal_long',
        ),
        migrations.RemoveField(
            model_name='nfl_team',
            name='o_field_goal_ratio',
        ),
        migrations.RemoveField(
            model_name='nfl_team',
            name='o_fifty_fg_ratio',
        ),
        migrations.RemoveField(
            model_name='nfl_team',
            name='o_fumbles',
        ),
        migrations.RemoveField(
            model_name='nfl_team',
            name='o_fumbles_lost',
        ),
        migrations.RemoveField(
            model_name='nfl_team',
            name='o_fumbles_recovered',
        ),
        migrations.RemoveField(
            model_name='nfl_team',
            name='o_interception_percentage',
        ),
        migrations.RemoveField(
            model_name='nfl_team',
            name='o_kick_fair_catches',
        ),
        migrations.RemoveField(
            model_name='nfl_team',
            name='o_kick_return_attempts',
        ),
        migrations.RemoveField(
            model_name='nfl_team',
            name='o_kick_return_average',
        ),
        migrations.RemoveField(
            model_name='nfl_team',
            name='o_kick_return_touchdowns',
        ),
        migrations.RemoveField(
            model_name='nfl_team',
            name='o_kick_return_yards',
        ),
        migrations.RemoveField(
            model_name='nfl_team',
            name='o_kicking_points',
        ),
        migrations.RemoveField(
            model_name='nfl_team',
            name='o_pass_attempts',
        ),
        migrations.RemoveField(
            model_name='nfl_team',
            name='o_pass_completions',
        ),
        migrations.RemoveField(
            model_name='nfl_team',
            name='o_passing_touchdown_percentage',
        ),
        migrations.RemoveField(
            model_name='nfl_team',
            name='o_passing_yards',
        ),
        migrations.RemoveField(
            model_name='nfl_team',
            name='o_passing_yards_per_attempt',
        ),
        migrations.RemoveField(
            model_name='nfl_team',
            name='o_punt_fair_catches',
        ),
        migrations.RemoveField(
            model_name='nfl_team',
            name='o_punt_return_attempts',
        ),
        migrations.RemoveField(
            model_name='nfl_team',
            name='o_punt_return_average',
        ),
        migrations.RemoveField(
            model_name='nfl_team',
            name='o_punt_return_touchdowns',
        ),
        migrations.RemoveField(
            model_name='nfl_team',
            name='o_punt_return_yards',
        ),
        migrations.RemoveField(
            model_name='nfl_team',
            name='o_receiver_targets',
        ),
        migrations.RemoveField(
            model_name='nfl_team',
            name='o_receiving_first_downs',
        ),
        migrations.RemoveField(
            model_name='nfl_team',
            name='o_receiving_touchdowns',
        ),
        migrations.RemoveField(
            model_name='nfl_team',
            name='o_receiving_yards',
        ),
        migrations.RemoveField(
            model_name='nfl_team',
            name='o_receiving_yards_per_game',
        ),
        migrations.RemoveField(
            model_name='nfl_team',
            name='o_reception_average',
        ),
        migrations.RemoveField(
            model_name='nfl_team',
            name='o_receptions',
        ),
        migrations.RemoveField(
            model_name='nfl_team',
            name='o_rushing_average',
        ),
        migrations.RemoveField(
            model_name='nfl_team',
            name='o_taken_sacks',
        ),
        migrations.RemoveField(
            model_name='nfl_team',
            name='o_thrown_interceptions',
        ),
        migrations.RemoveField(
            model_name='nfl_team',
            name='o_twenty_plus_yard_receptions',
        ),
        migrations.RemoveField(
            model_name='nfl_team',
            name='o_u_fortynine_fg_ratio',
        ),
        migrations.RemoveField(
            model_name='nfl_team',
            name='o_u_nineteen_fg_ratio',
        ),
        migrations.RemoveField(
            model_name='nfl_team',
            name='o_u_thritynine_fg_ratio',
        ),
        migrations.RemoveField(
            model_name='nfl_team',
            name='o_u_twentynine_fg_ratio',
        ),
        migrations.RemoveField(
            model_name='nfl_team',
            name='o_yards_after_catch',
        ),
        migrations.RemoveField(
            model_name='nfl_team',
            name='o_yards_lost',
        ),
        migrations.RemoveField(
            model_name='nfl_team',
            name='pass_attempts',
        ),
        migrations.RemoveField(
            model_name='nfl_team',
            name='pass_completions',
        ),
        migrations.RemoveField(
            model_name='nfl_team',
            name='passing_touchdown_percentage',
        ),
        migrations.RemoveField(
            model_name='nfl_team',
            name='passing_yards',
        ),
        migrations.RemoveField(
            model_name='nfl_team',
            name='passing_yards_per_attempt',
        ),
        migrations.RemoveField(
            model_name='nfl_team',
            name='punt_fair_catches',
        ),
        migrations.RemoveField(
            model_name='nfl_team',
            name='punt_return_attempts',
        ),
        migrations.RemoveField(
            model_name='nfl_team',
            name='punt_return_average',
        ),
        migrations.RemoveField(
            model_name='nfl_team',
            name='punt_return_touchdowns',
        ),
        migrations.RemoveField(
            model_name='nfl_team',
            name='punt_return_yards',
        ),
        migrations.RemoveField(
            model_name='nfl_team',
            name='receiver_targets',
        ),
        migrations.RemoveField(
            model_name='nfl_team',
            name='receiving_first_downs',
        ),
        migrations.RemoveField(
            model_name='nfl_team',
            name='receiving_touchdowns',
        ),
        migrations.RemoveField(
            model_name='nfl_team',
            name='receiving_yards',
        ),
        migrations.RemoveField(
            model_name='nfl_team',
            name='receiving_yards_per_game',
        ),
        migrations.RemoveField(
            model_name='nfl_team',
            name='reception_average',
        ),
        migrations.RemoveField(
            model_name='nfl_team',
            name='receptions',
        ),
        migrations.RemoveField(
            model_name='nfl_team',
            name='rushing_average',
        ),
        migrations.RemoveField(
            model_name='nfl_team',
            name='sacks_given',
        ),
        migrations.RemoveField(
            model_name='nfl_team',
            name='solo_tackles',
        ),
        migrations.RemoveField(
            model_name='nfl_team',
            name='taken_sacks',
        ),
        migrations.RemoveField(
            model_name='nfl_team',
            name='thrown_interceptions',
        ),
        migrations.RemoveField(
            model_name='nfl_team',
            name='total_tackles',
        ),
        migrations.RemoveField(
            model_name='nfl_team',
            name='twenty_plus_yard_receptions',
        ),
        migrations.RemoveField(
            model_name='nfl_team',
            name='u_fortynine_fg_ratio',
        ),
        migrations.RemoveField(
            model_name='nfl_team',
            name='u_nineteen_fg_ratio',
        ),
        migrations.RemoveField(
            model_name='nfl_team',
            name='u_thritynine_fg_ratio',
        ),
        migrations.RemoveField(
            model_name='nfl_team',
            name='u_twentynine_fg_ratio',
        ),
        migrations.RemoveField(
            model_name='nfl_team',
            name='yards_after_catch',
        ),
        migrations.RemoveField(
            model_name='nfl_team',
            name='yards_after_interceptions',
        ),
        migrations.RemoveField(
            model_name='nfl_team',
            name='yards_lost',
        ),
        migrations.AddField(
            model_name='nfl_team',
            name='average_interception_yards',
            field=models.DecimalField(blank=True, decimal_places=1, max_digits=4, null=True),
        ),
        migrations.AddField(
            model_name='nfl_team',
            name='average_kickoff_return_yards',
            field=models.DecimalField(blank=True, decimal_places=1, max_digits=4, null=True),
        ),
        migrations.AddField(
            model_name='nfl_team',
            name='average_penalty_yards_per_game',
            field=models.DecimalField(blank=True, decimal_places=3, max_digits=6, null=True),
        ),
        migrations.AddField(
            model_name='nfl_team',
            name='average_punt_return_yards',
            field=models.DecimalField(blank=True, decimal_places=1, max_digits=4, null=True),
        ),
        migrations.AddField(
            model_name='nfl_team',
            name='fieldgoal_makes_to_attempts',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AddField(
            model_name='nfl_team',
            name='first_downs_by_penalty',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='nfl_team',
            name='fourth_down_efficiency',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AddField(
            model_name='nfl_team',
            name='fourth_down_percentage',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=4, null=True),
        ),
        migrations.AddField(
            model_name='nfl_team',
            name='fumbles_to_fumbles_lost',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AddField(
            model_name='nfl_team',
            name='interception_returns_to_yards',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AddField(
            model_name='nfl_team',
            name='interceptions',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='nfl_team',
            name='kickoff_returns_to_yards',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AddField(
            model_name='nfl_team',
            name='net_passing_yards',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='nfl_team',
            name='net_passing_yards_per_game',
            field=models.DecimalField(blank=True, decimal_places=1, max_digits=4, null=True),
        ),
        migrations.AddField(
            model_name='nfl_team',
            name='o_average_interception_yards',
            field=models.DecimalField(blank=True, decimal_places=1, max_digits=4, null=True),
        ),
        migrations.AddField(
            model_name='nfl_team',
            name='o_average_kickoff_return_yards',
            field=models.DecimalField(blank=True, decimal_places=1, max_digits=4, null=True),
        ),
        migrations.AddField(
            model_name='nfl_team',
            name='o_average_penalty_yards_per_game',
            field=models.DecimalField(blank=True, decimal_places=3, max_digits=6, null=True),
        ),
        migrations.AddField(
            model_name='nfl_team',
            name='o_average_punt_return_yards',
            field=models.DecimalField(blank=True, decimal_places=1, max_digits=4, null=True),
        ),
        migrations.AddField(
            model_name='nfl_team',
            name='o_fieldgoal_makes_to_attempts',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AddField(
            model_name='nfl_team',
            name='o_first_downs_by_penalty',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='nfl_team',
            name='o_fourth_down_efficiency',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AddField(
            model_name='nfl_team',
            name='o_fourth_down_percentage',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=4, null=True),
        ),
        migrations.AddField(
            model_name='nfl_team',
            name='o_fumbles_to_fumbles_lost',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AddField(
            model_name='nfl_team',
            name='o_interception_returns_to_yards',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AddField(
            model_name='nfl_team',
            name='o_interceptions',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='nfl_team',
            name='o_kickoff_returns_to_yards',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AddField(
            model_name='nfl_team',
            name='o_net_passing_yards',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='nfl_team',
            name='o_net_passing_yards_per_game',
            field=models.DecimalField(blank=True, decimal_places=1, max_digits=4, null=True),
        ),
        migrations.AddField(
            model_name='nfl_team',
            name='o_passing_completions_to_attempts',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AddField(
            model_name='nfl_team',
            name='o_passing_first_downs',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='nfl_team',
            name='o_punt_returns_to_yards',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AddField(
            model_name='nfl_team',
            name='o_sacks_to_yards_lost',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AddField(
            model_name='nfl_team',
            name='o_third_down_efficiency',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AddField(
            model_name='nfl_team',
            name='o_third_down_percentage',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=4, null=True),
        ),
        migrations.AddField(
            model_name='nfl_team',
            name='o_time_of_possession',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AddField(
            model_name='nfl_team',
            name='o_total_1st_downs',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='nfl_team',
            name='o_total_offensive_plays',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='nfl_team',
            name='o_total_penalties_to_yards',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AddField(
            model_name='nfl_team',
            name='o_total_points',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='nfl_team',
            name='o_total_points_per_game',
            field=models.DecimalField(blank=True, decimal_places=1, max_digits=4, null=True),
        ),
        migrations.AddField(
            model_name='nfl_team',
            name='o_total_touchdowns',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='nfl_team',
            name='o_total_yards',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='nfl_team',
            name='o_turnover_ratio',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AddField(
            model_name='nfl_team',
            name='o_yards_per_pass_attempt',
            field=models.DecimalField(blank=True, decimal_places=1, max_digits=4, null=True),
        ),
        migrations.AddField(
            model_name='nfl_team',
            name='o_yards_per_rush_attempt',
            field=models.DecimalField(blank=True, decimal_places=1, max_digits=4, null=True),
        ),
        migrations.AddField(
            model_name='nfl_team',
            name='passing_completions_to_attempts',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AddField(
            model_name='nfl_team',
            name='passing_first_downs',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='nfl_team',
            name='punt_returns_to_yards',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AddField(
            model_name='nfl_team',
            name='sacks_to_yards_lost',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AddField(
            model_name='nfl_team',
            name='third_down_efficiency',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AddField(
            model_name='nfl_team',
            name='third_down_percentage',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=4, null=True),
        ),
        migrations.AddField(
            model_name='nfl_team',
            name='time_of_possession',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AddField(
            model_name='nfl_team',
            name='total_1st_downs',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='nfl_team',
            name='total_offensive_plays',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='nfl_team',
            name='total_penalties_to_yards',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AddField(
            model_name='nfl_team',
            name='total_points',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='nfl_team',
            name='total_points_per_game',
            field=models.DecimalField(blank=True, decimal_places=1, max_digits=4, null=True),
        ),
        migrations.AddField(
            model_name='nfl_team',
            name='total_touchdowns',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='nfl_team',
            name='total_yards',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='nfl_team',
            name='turnover_ratio',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AddField(
            model_name='nfl_team',
            name='yards_per_pass_attempt',
            field=models.DecimalField(blank=True, decimal_places=1, max_digits=4, null=True),
        ),
        migrations.AddField(
            model_name='nfl_team',
            name='yards_per_rush_attempt',
            field=models.DecimalField(blank=True, decimal_places=1, max_digits=4, null=True),
        )
    ]
