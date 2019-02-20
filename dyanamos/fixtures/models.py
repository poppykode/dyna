from django.db import models

# Create your models here.

class Team(models.Model):
    logo = models.ImageField(upload_to='logo/',null=True, blank =True )
    name = models.CharField(max_length=255, blank=True)
    
    def __str__(self):
        return self.name

class Tournament(models.Model):
    name = models.CharField(max_length=255,blank=True, null=True)

    def __str__(self):
        return self.name


class Fixture(models.Model):
    TYPES=(
        ("Home","Home"),
        ("Away","Away"),
    )
   
    home_or_away =models.CharField(max_length=20,choices=TYPES)
    tournament = models.ForeignKey(Tournament,on_delete=models.CASCADE,related_name='tournament_1')
    opponent1 =  models.ForeignKey(Team,on_delete=models.CASCADE,related_name='team_1')
    opponent2 = models.ForeignKey(Team,on_delete=models.CASCADE,related_name='team_2')
    venue = models.CharField(max_length=255, blank=True)
    date_created = models.DateTimeField(null=True)
    tournament_date = models.DateField(null=True)
    
    def __str__(self):
        return self.opponent1.name +' vs '+ self.opponent2.name

    class Meta:
        ordering = ["date_created",]



class Log(models.Model):
    position =  models.CharField(max_length=255, blank=True)
    team =  models.ForeignKey(Team,on_delete=models.CASCADE,related_name='team')
    played = models.CharField(max_length=255, blank=True)
    won = models.CharField(max_length=255, blank=True)
    draws = models.CharField(max_length=255, blank=True)
    lost = models.CharField(max_length=255, blank=True)
    goal_forward = models.CharField(max_length=255, blank=True)
    goal_against = models.CharField(max_length=255, blank=True)
    goal_difference = models.CharField(max_length=255, blank=True)
    points =  models.PositiveIntegerField()
    date_created = models.DateTimeField(null=True)
    
    def __str__(self):
        return self.team.name

    class Meta:
        ordering = ["position",]



class Result(models.Model):
    tournament =   models.ForeignKey(Tournament,on_delete=models.CASCADE,related_name='tournament_2')
    opponent1 =  models.ForeignKey(Team,on_delete=models.CASCADE,related_name='opponent_1')
    opponent2 = models.ForeignKey(Team,on_delete=models.CASCADE,related_name='opponent_2')
    opponent1_score =  models.CharField(max_length=255,blank=True, null=True)
    opponent2_score  =  models.CharField(max_length=255,blank=True, null=True)
    venue = models.CharField(max_length=255, blank=True)
    time =  models.DateTimeField(null=True)
    date_created = models.DateTimeField(null=True)
    
    def __str__(self):
        return self.opponent1.name +' '+ self.opponent1_score +' ' +' vs '+ self.opponent2.name +' '+ self.opponent2_score 

    class Meta:
        ordering = ["date_created",]


     







