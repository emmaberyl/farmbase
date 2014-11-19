# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('github', '0003_auto_20141119_2300'),
    ]

    operations = [
        migrations.CreateModel(
            name='GitHubRequestCache',
            fields=[
                ('query', models.CharField(max_length=255, serialize=False, primary_key=True)),
                ('ETag', models.CharField(max_length=255)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.DeleteModel(
            name='GitHubRequest',
        ),
        migrations.RemoveField(
            model_name='ratelimit',
            name='id',
        ),
        migrations.RemoveField(
            model_name='repo',
            name='pulls_Etag',
        ),
        migrations.AlterField(
            model_name='ratelimit',
            name='type',
            field=models.CharField(max_length=255, serialize=False, primary_key=True),
            preserve_default=True,
        ),
    ]
