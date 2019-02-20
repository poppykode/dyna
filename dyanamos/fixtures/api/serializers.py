from rest_framework import serializers
from fixtures.models import (
    Fixture,Log,Result,
) 

class FixtureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fixture
        fields = ('id', 'home_or_away', 'tournament', 'opponent1', 'opponent2','venue','tournament_date','date_created')

class LogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Log
        fields = ('id', 'position', 'team', 'played', 'won','draws','lost','goal_forward','goal_against','goal_difference','points','date_created')

class ResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = Result
        fields = ('id', 'tournament', 'opponent1', 'opponent2', 'opponent1_score','opponent2_score','venue','time','date_created')