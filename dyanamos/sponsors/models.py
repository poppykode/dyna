from django.db import models

# Create your models here.
class Sponsors(models.Model):
    name = models.CharField(max_length=255, blank=True)
    logo = models.ImageField(upload_to='logo/',null=True, blank =True )
    logo1 =models.ImageField(upload_to='logo/',null=True, blank =True )
    url = models.URLField(null=True, blank=True)
    date_created = models.DateTimeField(null=True)
    
    def __str__(self):
        return self.name

    class Meta:
        ordering = ["date_created",]
        verbose_name_plural = "Sponsors"