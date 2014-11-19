# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('repo', '0002_repo_last_modified'),
    ]

    operations = [
        migrations.AlterField(
            model_name='repo',
            name='fork_count',
            field=models.IntegerField(null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='repo',
            name='stargazer_count',
            field=models.IntegerField(null=True),
            preserve_default=True,
        ),
    ]
