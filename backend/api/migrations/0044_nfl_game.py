# Generated by Django 4.2.11 on 2024-07-01 14:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0043_nfl_team_o_yards_per_game_nfl_team_yards_per_game_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='NFL_Game',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('GID', models.CharField(max_length=10)),
                ('winner', models.CharField(blank=True, max_length=10, null=True)),
                ('score', models.CharField(blank=True, max_length=10, null=True)),
                ('spread', models.CharField(blank=True, max_length=10, null=True)),
                ('over_under', models.CharField(blank=True, max_length=10, null=True)),
                ('qb_passing_yards', models.IntegerField(blank=True, null=True)),
                ('qb_passing_touchdowns', models.IntegerField(blank=True, null=True)),
                ('rb_carries', models.IntegerField(blank=True, null=True)),
                ('rb_rushing_yards', models.IntegerField(blank=True, null=True)),
                ('rb_rushing_touchdowns', models.IntegerField(blank=True, null=True)),
                ('wr_receptions', models.IntegerField(blank=True, null=True)),
                ('wr_receiving_yards', models.IntegerField(blank=True, null=True)),
                ('wr_receiving_touchdowns', models.IntegerField(blank=True, null=True)),
                ('LYID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.league')),
                ('favorite', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='favorite_team', to='api.nfl_team')),
                ('qb', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='best_qb', to='api.nfl_player')),
                ('qb_team', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='qb_team', to='api.nfl_team')),
                ('rb', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='best_rb', to='api.nfl_player')),
                ('rb_team', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='rb_team', to='api.nfl_team')),
                ('underdog', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='underdog_team', to='api.nfl_team')),
                ('wr', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='best_wr', to='api.nfl_player')),
                ('wr_team', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='wr_team', to='api.nfl_team')),
            ],
        ),
    ]