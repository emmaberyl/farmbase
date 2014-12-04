# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('farmlyvore', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='food',
            old_name='food',
            new_name='food_name',
        ),
        migrations.RenameField(
            model_name='foodlink',
            old_name='food',
            new_name='food_name',
        ),
        migrations.RenameField(
            model_name='foodlink',
            old_name='place',
            new_name='place_name',
        ),
        migrations.RenameField(
            model_name='foodlink',
            old_name='season',
            new_name='season_name',
        ),
        migrations.RenameField(
            model_name='place',
            old_name='place',
            new_name='place_name',
        ),
        migrations.RenameField(
            model_name='season',
            old_name='approx_date',
            new_name='season_date',
        ),
        migrations.RenameField(
            model_name='season',
            old_name='season',
            new_name='season_name',
        ),
        migrations.RemoveField(
            model_name='place',
            name='zipcode',
        ),
    ]
