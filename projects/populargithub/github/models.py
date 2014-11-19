from django.db import models

# Create your models here.
class RepoQueue(models.Model):
    started_at = models.DateTimeField()
    completed_at = models.DateTimeField(default=None, null=True)
    repos_found = models.IntegerField(default=0)
    repos_processed = models.IntegerField(default=0)
    repos_skipped = models.IntegerField(default=0)
    
class RepoRequest(models.Model):
    repoqueue = models.ForeignKey(RepoQueue)
    since = models.IntegerField()
    Etag = models.CharField(max_length=255)
    
class RateLimit(models.Model):
    type = models.CharField(max_length=255)
    limit = models.IntegerField()
    remaining = models.IntegerField()
    reset = models.DateTimeField()
    
class Repo(models.Model):
    # core stats
    id = models.IntegerField(primary_key=True)
    full_name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    html_url = models.CharField(max_length=255)
    #used for rate limiting
    pulls_Etag = models.CharField(max_length=255, default=None, null=True)
    #pulls_Last_Modified = models.DateTimeField(null=True, default=None)
    
    # verify field below:
    # api_url = models.CharField(max_length=255)
    # fields below are not worth an api hit I think
    stargazer_count = models.IntegerField(null=True)
    fork_count = models.IntegerField(null=True)
    # more foreign keys?
    #collaborator_count -- fk or count?
    #commits - fk - timestamped, author
class User(models.Model):
    id = models.IntegerField(primary_key=True)
    login = models.CharField(max_length=255)
    
class PullRequest(models.Model):
    repo = models.ForeignKey(Repo)
    number = models.IntegerField(primary_key=True)
    user = models.ForeignKey(User)
    state = models.CharField(max_length=255)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    closed_at = models.DateTimeField(null=True) 
    merged_at = models.DateTimeField(null=True)

# TODO: Issue Stats.  Skipping this to keep scope simpler.    
# class Issue(models.Model):
    # repo = models.ForeignKey(Repo)
    # number = models.IntegerField()
    # state = models.CharField(max_length=255)
    # created_at = models.DateTimeField()
    # closed_at = models.DateTimeField()
    # updated_at = models.DateTimeField()
    # derived fields
    # reopen_count = models.IntegerField()
    # response_count = models.IntegerField()