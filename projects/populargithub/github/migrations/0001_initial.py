# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RateLimit',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('type', models.CharField(max_length=255)),
                ('limit', models.IntegerField()),
                ('remaining', models.IntegerField()),
                ('reset', models.DateTimeField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='RepoQueue',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('started_at', models.DateTimeField()),
                ('completed_at', models.DateTimeField(default=None, null=True)),
                ('repos_found', models.IntegerField(default=0)),
                ('repos_processed', models.IntegerField(default=0)),
                ('repos_skipped', models.IntegerField(default=0)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='RepoRequest',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('since', models.IntegerField()),
                ('Etag', models.CharField(max_length=255)),
                ('repoqueue', models.ForeignKey(to='github.RepoQueue')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
