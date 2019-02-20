from rest_framework import serializers
from team.models import (
    CurrentTeam,
) 

class CurrentTeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = CurrentTeam
        fields = ('id', 'position', 'name', 'surname', 'number','image','bio','date_of_birth','nationality','height','weight','facebook','twitter','date_created')
