from django.db import models

# Create your models here.
class Slider(models.Model):
    background_image = models.ImageField(upload_to='slider/',null=True, blank =True )
    heading = models.CharField(max_length=255, blank=True)
    heading_color = models.CharField(max_length=255, blank=True,default='#31387D')
    description = models.TextField()
    description_color = models.CharField(max_length=255, blank=True,default='#31387D')
    button_text = models.CharField(max_length=255, blank=True)
    button_link = models.URLField(null=True, blank=True)
    priority = models.PositiveIntegerField()
    
    def __str__(self):
        return self.heading

    class Meta:
        ordering = ["priority",]
