import json, logging
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, Http404, HttpResponseRedirect, HttpResponseBadRequest
from django.core.urlresolvers import reverse
from django.views import generic
from farmlyvore.models import Food

def index(request):
    food_list = Food.objects.all()#.order_by('food')[:5]
    context = { 'food_list': food_list }
    return render(request, 'farmlyvore/index.html', context)
