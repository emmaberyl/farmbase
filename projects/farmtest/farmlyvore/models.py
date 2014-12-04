from django.db import models

# Create your models here.
class Food(models.Model):
    food_name = models.CharField(max_length=200)
    food_url = models.URLField(max_length=1000)
    def __unicode__(self):
        return self.food_name

class Place(models.Model):
    place_name = models.CharField(max_length=200)
    def __unicode__(self):
        return self.place_name

class Season(models.Model):
    season_name = models.CharField(max_length=200)
    season_date = models.DateField()
    def __unicode__(self):
        return self.season_name

class FoodLink(models.Model):
    food_name = models.ForeignKey(Food)
    place_name = models.ForeignKey(Place)
    season_name = models.ForeignKey(Season)
    def __unicode__(self):
        return "{0} has {1} in {2}!".format(self.place_name.place_name,self.food_name.food_name,self.season_name.season_name)


