# Generated by Django 4.2.11 on 2024-06-28 14:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0040_remove_nfl_player_extra_point_percetage_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nfl_player',
            name='link',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
    ]
