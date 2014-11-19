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