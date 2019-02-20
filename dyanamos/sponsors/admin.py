from django.contrib import admin
from django.utils import timezone
from .models import (   
    Sponsors,
)

# Register your models here.

class SponsorsAdmin(admin.ModelAdmin):
    
    readonly_fields = ('date_created',)

    def save_model(self, request, obj, form, change):
        obj.date_created = timezone.now()
        super(SponsorsAdmin, self).save_model(request, obj, form, change)

admin.site.register(Sponsors, SponsorsAdmin)

