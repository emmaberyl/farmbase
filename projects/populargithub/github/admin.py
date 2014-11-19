from django.contrib import admin
from github.models import *

# Register your models here.
admin.site.register(RepoQueue)
admin.site.register(RateLimit)