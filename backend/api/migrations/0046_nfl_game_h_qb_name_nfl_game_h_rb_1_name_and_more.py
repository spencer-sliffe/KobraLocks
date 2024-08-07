# Generated by Django 4.2.11 on 2024-07-02 20:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0045_remove_nfl_game_qb_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='nfl_game',
            name='h_qb_name',
            field=models.CharField(blank=True, max_length=60, null=True),
        ),
        migrations.AddField(
            model_name='nfl_game',
            name='h_rb_1_name',
            field=models.CharField(blank=True, max_length=60, null=True),
        ),
        migrations.AddField(
            model_name='nfl_game',
            name='h_rb_2_name',
            field=models.CharField(blank=True, max_length=60, null=True),
        ),
        migrations.AddField(
            model_name='nfl_game',
            name='h_wr_1_name',
            field=models.CharField(blank=True, max_length=60, null=True),
        ),
        migrations.AddField(
            model_name='nfl_game',
            name='h_wr_2_name',
            field=models.CharField(blank=True, max_length=60, null=True),
        ),
        migrations.AddField(
            model_name='nfl_game',
            name='v_qb_name',
            field=models.CharField(blank=True, max_length=60, null=True),
        ),
        migrations.AddField(
            model_name='nfl_game',
            name='v_rb_1_name',
            field=models.CharField(blank=True, max_length=60, null=True),
        ),
        migrations.AddField(
            model_name='nfl_game',
            name='v_rb_2_name',
            field=models.CharField(blank=True, max_length=60, null=True),
        ),
        migrations.AddField(
            model_name='nfl_game',
            name='v_wr_1_name',
            field=models.CharField(blank=True, max_length=60, null=True),
        ),
        migrations.AddField(
            model_name='nfl_game',
            name='v_wr_2_name',
            field=models.CharField(blank=True, max_length=60, null=True),
        ),
    ]
