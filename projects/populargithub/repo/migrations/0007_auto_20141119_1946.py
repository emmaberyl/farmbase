# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('repo', '0006_auto_20141118_0307'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='repo',
            name='pulls_Last_Modified',
        ),
        migrations.AlterField(
            model_name='repo',
            name='pulls_Etag',
            field=models.CharField(default=None, max_length=255, null=True),
            preserve_default=True,
        ),
    ]
