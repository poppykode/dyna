from django.db import models

# Create your models here.
class CurrentTeam(models.Model):
    TYPES=(
        ("select","Select"),
        ("Goalkeeper","Goalkeeper"),
        ("Forward","Forward"),
        ("Midfielder","Midfielder"),
        ("Defender","Defender"),
    )
   
    position =  models.CharField(max_length=20,choices=TYPES,default ="All")
    name = models.CharField(max_length=255, blank=True)
    surname = models.CharField(max_length=255, blank=True)
    number = models.CharField(max_length=255, blank=True)
    image = models.ImageField(upload_to='players/',null=True, blank =True)
    bio = models.TextField()
    date_of_birth = models.DateField()
    nationality = models.CharField(max_length=255, blank=True)
    height = models.CharField(max_length=255, blank=True)
    weight = models.CharField(max_length=255, blank=True)
    date_created = models.DateTimeField(null=True)
    facebook = models.URLField(null=True, blank=True)
    twitter = models.URLField(null=True, blank=True)
    
    def __str__(self):
        return self.name

    class Meta:
        ordering = ["date_created",]
        # verbose_name_plural = "Sponsors"