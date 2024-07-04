# Generated by Django 4.2.11 on 2024-06-10 14:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_alter_game_inning_state'),
    ]

    operations = [
        migrations.CreateModel(
            name='MLBGame',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('team1', models.CharField(max_length=100)),
                ('team2', models.CharField(max_length=100)),
                ('game_time', models.DateTimeField(blank=True, null=True)),
                ('live', models.BooleanField(default=False)),
                ('inning_state', models.CharField(blank=True, max_length=50, null=True)),
                ('team1_score', models.IntegerField(blank=True, null=True)),
                ('team2_score', models.IntegerField(blank=True, null=True)),
                ('balls', models.IntegerField(blank=True, null=True)),
                ('strikes', models.IntegerField(blank=True, null=True)),
                ('outs', models.IntegerField(blank=True, null=True)),
                ('team1_spread', models.CharField(blank=True, max_length=20, null=True)),
                ('team2_spread', models.CharField(blank=True, max_length=20, null=True)),
                ('team1_total', models.CharField(blank=True, max_length=20, null=True)),
                ('team2_total', models.CharField(blank=True, max_length=20, null=True)),
                ('team1_money', models.CharField(blank=True, max_length=20, null=True)),
                ('team2_money', models.CharField(blank=True, max_length=20, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='MLSGame',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('team1', models.CharField(max_length=100)),
                ('team2', models.CharField(max_length=100)),
                ('team1_record', models.CharField(max_length=100)),
                ('team2_record', models.CharField(max_length=100)),
                ('game_time', models.DateTimeField(blank=True, null=True)),
                ('live', models.BooleanField(default=False)),
                ('clock', models.CharField(blank=True, max_length=50, null=True)),
                ('team1_score', models.IntegerField(blank=True, null=True)),
                ('team2_score', models.IntegerField(blank=True, null=True)),
                ('team1_spread', models.CharField(blank=True, max_length=20, null=True)),
                ('team2_spread', models.CharField(blank=True, max_length=20, null=True)),
                ('team1_total', models.CharField(blank=True, max_length=20, null=True)),
                ('team2_total', models.CharField(blank=True, max_length=20, null=True)),
                ('team1_money', models.CharField(blank=True, max_length=20, null=True)),
                ('team2_money', models.CharField(blank=True, max_length=20, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='NBAGame',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('team1', models.CharField(max_length=100)),
                ('team2', models.CharField(max_length=100)),
                ('game_time', models.DateTimeField(blank=True, null=True)),
                ('live', models.BooleanField(default=False)),
                ('quarter_state', models.CharField(blank=True, max_length=50, null=True)),
                ('clock', models.CharField(blank=True, max_length=50, null=True)),
                ('team1_score', models.IntegerField(blank=True, null=True)),
                ('team2_score', models.IntegerField(blank=True, null=True)),
                ('team1_spread', models.CharField(blank=True, max_length=20, null=True)),
                ('team2_spread', models.CharField(blank=True, max_length=20, null=True)),
                ('team1_total', models.CharField(blank=True, max_length=20, null=True)),
                ('team2_total', models.CharField(blank=True, max_length=20, null=True)),
                ('team1_money', models.CharField(blank=True, max_length=20, null=True)),
                ('team2_money', models.CharField(blank=True, max_length=20, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='NCAABaskBallGame',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('team1', models.CharField(max_length=100)),
                ('team2', models.CharField(max_length=100)),
                ('game_time', models.DateTimeField(blank=True, null=True)),
                ('live', models.BooleanField(default=False)),
                ('quarter_state', models.CharField(blank=True, max_length=50, null=True)),
                ('clock', models.CharField(blank=True, max_length=50, null=True)),
                ('team1_score', models.IntegerField(blank=True, null=True)),
                ('team2_score', models.IntegerField(blank=True, null=True)),
                ('team1_spread', models.CharField(blank=True, max_length=20, null=True)),
                ('team2_spread', models.CharField(blank=True, max_length=20, null=True)),
                ('team1_total', models.CharField(blank=True, max_length=20, null=True)),
                ('team2_total', models.CharField(blank=True, max_length=20, null=True)),
                ('team1_money', models.CharField(blank=True, max_length=20, null=True)),
                ('team2_money', models.CharField(blank=True, max_length=20, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='NCAABBGame',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('team1', models.CharField(max_length=100)),
                ('team2', models.CharField(max_length=100)),
                ('game_time', models.DateTimeField(blank=True, null=True)),
                ('live', models.BooleanField(default=False)),
                ('inning_state', models.CharField(blank=True, max_length=50, null=True)),
                ('team1_score', models.IntegerField(blank=True, null=True)),
                ('team2_score', models.IntegerField(blank=True, null=True)),
                ('balls', models.IntegerField(blank=True, null=True)),
                ('strikes', models.IntegerField(blank=True, null=True)),
                ('outs', models.IntegerField(blank=True, null=True)),
                ('team1_spread', models.CharField(blank=True, max_length=20, null=True)),
                ('team2_spread', models.CharField(blank=True, max_length=20, null=True)),
                ('team1_total', models.CharField(blank=True, max_length=20, null=True)),
                ('team2_total', models.CharField(blank=True, max_length=20, null=True)),
                ('team1_money', models.CharField(blank=True, max_length=20, null=True)),
                ('team2_money', models.CharField(blank=True, max_length=20, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='NCAAFBGame',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('team1', models.CharField(max_length=100)),
                ('team2', models.CharField(max_length=100)),
                ('game_time', models.DateTimeField(blank=True, null=True)),
                ('live', models.BooleanField(default=False)),
                ('quarter_state', models.CharField(blank=True, max_length=50, null=True)),
                ('clock', models.CharField(blank=True, max_length=50, null=True)),
                ('team1_score', models.IntegerField(blank=True, null=True)),
                ('team2_score', models.IntegerField(blank=True, null=True)),
                ('team1_spread', models.CharField(blank=True, max_length=20, null=True)),
                ('team2_spread', models.CharField(blank=True, max_length=20, null=True)),
                ('team1_total', models.CharField(blank=True, max_length=20, null=True)),
                ('team2_total', models.CharField(blank=True, max_length=20, null=True)),
                ('team1_money', models.CharField(blank=True, max_length=20, null=True)),
                ('team2_money', models.CharField(blank=True, max_length=20, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='NFLGame',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('team1', models.CharField(max_length=100)),
                ('team2', models.CharField(max_length=100)),
                ('game_time', models.DateTimeField(blank=True, null=True)),
                ('live', models.BooleanField(default=False)),
                ('quarter_state', models.CharField(blank=True, max_length=50, null=True)),
                ('clock', models.CharField(blank=True, max_length=50, null=True)),
                ('team1_score', models.IntegerField(blank=True, null=True)),
                ('team2_score', models.IntegerField(blank=True, null=True)),
                ('team1_spread', models.CharField(blank=True, max_length=20, null=True)),
                ('team2_spread', models.CharField(blank=True, max_length=20, null=True)),
                ('team1_total', models.CharField(blank=True, max_length=20, null=True)),
                ('team2_total', models.CharField(blank=True, max_length=20, null=True)),
                ('team1_money', models.CharField(blank=True, max_length=20, null=True)),
                ('team2_money', models.CharField(blank=True, max_length=20, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='WNBAGame',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('team1', models.CharField(max_length=100)),
                ('team2', models.CharField(max_length=100)),
                ('game_time', models.DateTimeField(blank=True, null=True)),
                ('live', models.BooleanField(default=False)),
                ('quarter_state', models.CharField(blank=True, max_length=50, null=True)),
                ('clock', models.CharField(blank=True, max_length=50, null=True)),
                ('team1_score', models.IntegerField(blank=True, null=True)),
                ('team2_score', models.IntegerField(blank=True, null=True)),
                ('team1_spread', models.CharField(blank=True, max_length=20, null=True)),
                ('team2_spread', models.CharField(blank=True, max_length=20, null=True)),
                ('team1_total', models.CharField(blank=True, max_length=20, null=True)),
                ('team2_total', models.CharField(blank=True, max_length=20, null=True)),
                ('team1_money', models.CharField(blank=True, max_length=20, null=True)),
                ('team2_money', models.CharField(blank=True, max_length=20, null=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Game',
        ),
    ]
