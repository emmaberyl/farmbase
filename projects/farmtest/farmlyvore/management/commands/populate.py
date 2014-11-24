import csv
import psycopg2
from django.core.management.base import BaseCommand
from farmlyvore.models import Food, Place, Season, FoodLink
from django.utils import timezone

class Command(BaseCommand):

    def handle(self, *args, **options):

        infile = "/projects/seasonalfooddb.csv"

        with open(infile, 'r') as f:
            data = [row for row in csv.reader(f.read().splitlines())]

        for row in data:
            thisfood = row[0].strip()
            thisseason = row[1].strip()
            thisplace = row[2].strip()

            f = Food.objects.filter(food=thisfood)
            if not f:
                f = Food(food=thisfood)
                f.save()
            else:
                f = Food.objects.get(id=f)

            p = Place.objects.filter(place=thisplace)
            if not p:
                p = Place(place=thisplace,zipcode=00000)
                p.save()
            else:
                p = Place.objects.get(id=p)

            s = Season.objects.filter(season=thisseason)
            if not s:
                s = Season(season=thisseason, approx_date=timezone.now())
                s.save()
            else:
                s = Season.objects.get(id=s)

            n = FoodLink.objects.filter(food=f,place=p,season=s)
            if not n:
                n = FoodLink(food=f,place=p,season=s)
                n.save()
                self.stdout.write("added record: " + str(n))
            else:
                self.stdout.write("skipping duplicate: " + str(n))












