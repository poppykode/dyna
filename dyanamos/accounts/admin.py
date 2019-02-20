from django.contrib import admin
from django.utils import timezone
from .models import (
    UploadGamePromo,Loyalty,
)

# Register your models here.

class UploadGamePromoAdmin(admin.ModelAdmin):
    
    readonly_fields = ('date_created',)

    def save_model(self, request, obj, form, change):
        obj.date_created = timezone.now()
        super(UploadGamePromoAdmin, self).save_model(request, obj, form, change)

admin.site.register(UploadGamePromo, UploadGamePromoAdmin)
admin.site.register(Loyalty)

