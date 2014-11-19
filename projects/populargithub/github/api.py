from tastypie.resources import ModelResource
from github.models import RateLimit

class RateLimitResource(ModelResource):
    class Meta:
        queryset = RateLimit.objects.all()
        resource_name = 'ratelimit'