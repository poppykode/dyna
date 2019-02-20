from django.contrib import admin
from django.utils import timezone
from .models import (   
    Fixture, Team,Log,
    Result,Tournament,
)

# Register your models here.

class FixtureAdmin(admin.ModelAdmin):
    
    readonly_fields = ('date_created',)

    def save_model(self, request, obj, form, change):
        obj.date_created = timezone.now()
        super(FixtureAdmin, self).save_model(request, obj, form, change)

class LogAdmin(admin.ModelAdmin):
    
    readonly_fields = ('date_created',)

    def save_model(self, request, obj, form, change):
        obj.date_created = timezone.now()
        super(LogAdmin, self).save_model(request, obj, form, change)

class ResultAdmin(admin.ModelAdmin):
    
    readonly_fields = ('date_created',)

    def save_model(self, request, obj, form, change):
        obj.date_created = timezone.now()
        super(ResultAdmin, self).save_model(request, obj, form, change)


admin.site.register(Fixture, FixtureAdmin)
admin.site.register(Log,LogAdmin)
admin.site.register(Result,ResultAdmin)
admin.site.register(Team)
admin.site.register(Tournament)
