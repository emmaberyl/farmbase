from django.db import models

# Create your models here.
class Food(models.Model):
    food = models.CharField(max_length=200)
    food_url = models.URLField(max_length=1000)
    def __unicode__(self):
        return self.food

class Place(models.Model):
    place = models.CharField(max_length=200)
    zipcode = models.IntegerField()
    def __unicode__(self):
        return self.place

class Season(models.Model):
    season = models.CharField(max_length=200)
    approx_date = models.DateField()
    def __unicode__(self):
        return self.season

class FoodLink(models.Model):
    food = models.ForeignKey(Food)
    place = models.ForeignKey(Place)
    season = models.ForeignKey(Season)
    def __unicode__(self):
        return "{0} has {1} in {2}!".format(self.place.place,self.food.food,self.season.season)


