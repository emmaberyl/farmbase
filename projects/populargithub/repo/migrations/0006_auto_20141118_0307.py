# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('repo', '0005_auto_20141118_0306'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pullrequest',
            name='merged_at',
            field=models.DateTimeField(null=True),
            preserve_default=True,
        ),
    ]
