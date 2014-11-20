from django.contrib import admin
from github.models import *

class RateLimitAdmin(admin.ModelAdmin):
    list_display = ('type','limit','remaining','reset')

class GitHubRequestCacheAdmin(admin.ModelAdmin):
    list_display = ('query','ETag')
    
# Register your models here.
admin.site.register(RepoQueue)
admin.site.register(RateLimit, RateLimitAdmin)
#admin.site.register(Repo)
admin.site.register(GitHubRequestCache,GitHubRequestCacheAdmin)

