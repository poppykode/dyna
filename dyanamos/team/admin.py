from django.contrib import admin
from django.utils import timezone
from .models import (   
    CurrentTeam,
)

# Register your models here.

class CurrentTeamAdmin(admin.ModelAdmin):
    
    readonly_fields = ('date_created',)

    def save_model(self, request, obj, form, change):
        obj.date_created = timezone.now()
        super(CurrentTeamAdmin, self).save_model(request, obj, form, change)

admin.site.register(CurrentTeam, CurrentTeamAdmin)

