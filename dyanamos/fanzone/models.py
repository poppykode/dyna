from django.db import models


# Create your models here.
class Photo(models.Model):
    image = models.ImageField(upload_to='fan/photos',null=True, blank =True )
    heading = models.CharField(max_length=255, blank=True)
    date_created = models.DateTimeField(null=True)
    
    def __str__(self):
        return self.heading

    class Meta:
        ordering = ["date_created",]


class Video(models.Model):
    cover_image = models.ImageField(upload_to='fan/videos',null=True, blank =True )
    heading = models.CharField(max_length=255, blank=True)
    date_created = models.DateTimeField(null=True)
    url = models.URLField(null=True, blank=True)
    
    def __str__(self):
        return self.heading

    class Meta:
        ordering = ["date_created",]


