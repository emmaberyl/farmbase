# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('github', '0002_auto_20141119_2248'),
    ]

    operations = [
        migrations.CreateModel(
            name='GitHubRequest',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('query', models.CharField(max_length=255)),
                ('Etag', models.CharField(max_length=255)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='reporequest',
            name='repoqueue',
        ),
        migrations.DeleteModel(
            name='RepoRequest',
        ),
    ]
