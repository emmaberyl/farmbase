# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('github', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PullRequest',
            fields=[
                ('number', models.IntegerField(serialize=False, primary_key=True)),
                ('state', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField()),
                ('updated_at', models.DateTimeField()),
                ('closed_at', models.DateTimeField(null=True)),
                ('merged_at', models.DateTimeField(null=True)),
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
                ('pulls_Etag', models.CharField(default=None, max_length=255, null=True)),
                ('stargazer_count', models.IntegerField(null=True)),
                ('fork_count', models.IntegerField(null=True)),
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
            field=models.ForeignKey(to='github.Repo'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='pullrequest',
            name='user',
            field=models.ForeignKey(to='github.User'),
            preserve_default=True,
        ),
    ]
