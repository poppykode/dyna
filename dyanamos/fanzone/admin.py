from django.contrib import admin
from django.utils import timezone
from .models import (   
    Photo,Video,
)

# Register your models here.

class PhotoAdmin(admin.ModelAdmin):
    
    readonly_fields = ('date_created',)

    def save_model(self, request, obj, form, change):
        obj.date_created = timezone.now()
        super(PhotoAdmin, self).save_model(request, obj, form, change)

class VideoAdmin(admin.ModelAdmin):
    
    readonly_fields = ('date_created',)

    def save_model(self, request, obj, form, change):
        obj.date_created = timezone.now()
        super(VideoAdmin, self).save_model(request, obj, form, change)

admin.site.register(Video, VideoAdmin)
admin.site.register(Photo, PhotoAdmin)

