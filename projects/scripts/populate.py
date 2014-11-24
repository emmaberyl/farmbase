import csv
import psycopg2
from django.core.management.base import BaseCommand
from farmlyvore.models import Food, Place, Season, FoodLink

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

            p = Place.objects.filter(place=thisplace)
            if not p:
                p = Place(place=thisplace,zipcode=00000)
                p.save()

            s = Season.objects.filter(season=thisseason)
            if not s:
                s = Season(season=thisseason)
                s.save()

            new_record = FoodLink(Food=idfood,Place=idplace,Season=idseason)
            new_record.save()

            self.stdout.write("added record: " + new_record)









