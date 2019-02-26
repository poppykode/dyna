from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import datetime    
from fixtures.models import Fixture


# Create your models here.

class User(AbstractUser):
    identification_number = models.CharField(max_length=255,blank=True, null=True)
    paid = models.BooleanField(default=False)
    sub_expiration_date = models.DateTimeField(default='2000-02-12 19:09:56.668926')
   
class UploadGamePromo(models.Model):
    user =  models.ForeignKey(User,on_delete=models.CASCADE)
    team_one = models.ForeignKey(Fixture,on_delete=models.CASCADE,related_name='fixture_one')
    team_two = models.ForeignKey(Fixture,on_delete=models.CASCADE,related_name='fixture_two')
    match_image = models.ImageField(upload_to='match-game/',null=True, blank =True)
    date_played = models.DateField()
    date_created = models.DateTimeField(null=True)
    published =  models.BooleanField(default=False)

    def __str__(self):
        return self.user.first_name

    class Meta:
        ordering = ["date_created",]

class FanOfTheMatch(models.Model):
    user =  models.ForeignKey(User,on_delete=models.CASCADE)
    name_of_fan =  models.CharField(max_length=255, blank=True)
    fan_image = models.ImageField(upload_to='fan/photo/',null=True, blank =True)
    date_created = models.DateTimeField(default=datetime.now(), blank=True)
    published =  models.BooleanField(default=False)
    votes = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name_of_fan

    class Meta:
        ordering = ["date_created",]

class ManOfTheMatch(models.Model):
    user =  models.ForeignKey(User,on_delete=models.CASCADE)
    name_of_man_of_the_match =  models.CharField(max_length=255, blank=True)
    man_of_the_match_image = models.ImageField(upload_to='fan/photo/',null=True, blank =True)
    date_created = models.DateTimeField(default=datetime.now())
    published =  models.BooleanField(default=False)
    votes = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name_of_man_of_the_match

    class Meta:
        ordering = ["date_created",]

class TravelWithTheTeam(models.Model):

    user =  models.ForeignKey(User,on_delete=models.CASCADE)
    team_caption =  models.CharField(max_length=255, blank=True)
    best_team_image = models.ImageField(upload_to='fan/photo/',null=True, blank =True)
    date_created = models.DateTimeField(default=datetime.now())
    published =  models.BooleanField(default=False)
    votes = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.team_caption

    class Meta:
        ordering = ["date_created",]

class Loyalty(models.Model):
    user =  models.ForeignKey(User,on_delete=models.CASCADE)
    venue = models.CharField(max_length=255, blank=True)
    teams_played = models.CharField(max_length=255, blank=True)
    tournament_date =  models.CharField(max_length=255, blank=True,default='Feb. 20, 2019')
    date_created = models.DateTimeField(default=datetime.now(), blank=True)
    points = models.PositiveIntegerField(default=0)
    
   

    def __str__(self):
        return self.user.first_name

    class Meta:
        ordering = ["date_created",]
        unique_together = ('user', 'teams_played', 'tournament_date')          


class MomementOfTheMatch(models.Model):

    user =  models.ForeignKey(User,on_delete=models.CASCADE)
    name_of_the_moment =  models.CharField(max_length=255, blank=True)
    image_of_the_moment = models.ImageField(upload_to='fan/photo/',null=True, blank =True)
    date_created = models.DateTimeField(default=datetime.now())
    published =  models.BooleanField(default=False)
    votes = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name_of_the_moment

    class Meta:
        ordering = ["date_created",]