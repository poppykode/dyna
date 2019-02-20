from django.db import models

# Create your models here.
class News(models.Model):
    image = models.ImageField(upload_to='news/',null=True, blank =True )
    heading = models.CharField(max_length=255, blank=True)
    description = models.TextField(null=True)
    date_created = models.DateTimeField(null=True)
    
    def __str__(self):
        return self.heading

    class Meta:
        ordering = ["-date_created",]
        verbose_name_plural = "News"


