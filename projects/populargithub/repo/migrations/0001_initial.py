# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PullRequest',
            fields=[
                ('number', models.IntegerField(serialize=False, primary_key=True)),
                ('state', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField()),
                ('updated_at', models.DateTimeField()),
                ('closed_at', models.DateTimeField()),
                ('merged_at', models.DateTimeField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Repo',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True)),
                ('full_name', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=255)),
                ('html_url', models.CharField(max_length=255)),
                ('Etag', models.CharField(max_length=255)),
                ('stargazer_count', models.IntegerField()),
                ('fork_count', models.IntegerField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True)),
                ('login', models.CharField(max_length=255)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='pullrequest',
            name='repo',
            field=models.ForeignKey(to='repo.Repo'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='pullrequest',
            name='user',
            field=models.ForeignKey(to='repo.User'),
            preserve_default=True,
        ),
    ]
