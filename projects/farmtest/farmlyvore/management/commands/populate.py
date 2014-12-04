import csv
from django.core.management.base import BaseCommand
from farmlyvore.models import Food, Place, Season, FoodLink
import calendar
import datetime

class Command(BaseCommand):

    def handle(self, *args, **options):

        infile = "/projects/seasonalfooddb.csv"

        #make month name dictionary
        months = dict((v,k) for k,v in enumerate(calendar.month_name))

        with open(infile, 'r') as f:
            data = [row for row in csv.reader(f.read().splitlines())]

        #for each row of data in the csv file
        for row in data:
            thisfood = row[0].strip()
            thisseason = row[1].strip()
            thisplace = row[2].strip()

            #check if an entry already exists for this food
            f = Food.objects.filter(food_name=thisfood)
            if not f:
                f = Food(food_name=thisfood)
                f.save()
            else:
                f = Food.objects.get(id=f)

            #check if an entry already exists for this place
            p = Place.objects.filter(place_name=thisplace)
            if not p:
                p = Place(place_name=thisplace)
                p.save()
            else:
                p = Place.objects.get(id=p)

            #check if an entry already exists for this season increment
            s = Season.objects.filter(season_name=thisseason)
            if not s:
                # example = 'January (early)'
                thismonth = months[thisseason[0:thisseason.find('(')-1]]
                if thisseason.find('early') > 0:
                    thisday = 1
                else:
                    thisday = 15
                thisdate = datetime.datetime.strptime('2015-{0}-{1}'.format(thismonth,thisday),'%Y-%m-%d').date()
                s = Season(season_name=thisseason, season_date=thisdate)
                s.save()
            else:
                s = Season.objects.get(id=s)

            #check if link already exists (some duplicates may arise due to collapsing across "Northern" and "Southern"
            n = FoodLink.objects.filter(food_name=f,place_name=p,season_name=s)
            if not n:
                n = FoodLink(food_name=f,place_name=p,season_name=s)
                n.save()
                # self.stdout.write("added record: " + str(n))
            # else:
                # self.stdout.write("skipping duplicate: " + str(n))












