# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('repo', '0003_auto_20141118_0159'),
    ]

    operations = [
        migrations.RenameField(
            model_name='repo',
            old_name='Last_Modified',
            new_name='pulls_Last_Modified',
        ),
        migrations.RemoveField(
            model_name='repo',
            name='Etag',
        ),
        migrations.AddField(
            model_name='repo',
            name='pulls_Etag',
            field=models.CharField(default=None, max_length=255),
            preserve_default=True,
        ),
    ]
