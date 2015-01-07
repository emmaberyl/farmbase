import json, logging
import sys
import datetime, calendar
from dateutil.relativedelta import relativedelta
from django.utils import timezone
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, Http404, HttpResponseRedirect, HttpResponseBadRequest
from django.core.urlresolvers import reverse
from django.views import generic
from farmlyvore.models import Food, FoodLink, Place, Season

def index(request):
    food_list = Food.objects.all()#.order_by('food')[:5]
    context = { 'food_list': food_list }
    return render(request, 'farmlyvore/index.html', context)

def date_helper():
    today = datetime.date.today()

    if today.year == 2014:
        today += relativedelta(years=1)

    first_day_of_the_month = datetime.date(today.year,today.month, 1)
    mid_day_of_the_month = datetime.date(today.year,today.month, 15)

    if today < mid_day_of_the_month:
        return first_day_of_the_month
    else:
        return mid_day_of_the_month


def search(request):
    if request.method == 'GET':

        response_data = {}
        season = date_helper()
        state_name = request.GET.get('statecode')
        food_list = FoodLink.objects.filter(place_name__place_name=state_name, season_name__season_date=season)[:10]
        food_results = [d.food_name.food_name + " " + d.season_name.season_date.strftime("%Y-%m-%d") for d in food_list]

        response_data['result'] = food_results
        return HttpResponse(
            json.dumps(response_data),
            content_type="application/json"
        )
    else:
        message = "OOPS, something went wrong"
    return render(request, 'farmlyvore/index.html', message)
