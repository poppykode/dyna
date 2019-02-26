from rest_framework import serializers
from fixtures.models import (
    Fixture,Log,Result,
) 

class FixtureSerializer(serializers.ModelSerializer):
    tournament = serializers.CharField(source="tournament.name")
    opponent_logo1= serializers.CharField(source="opponent1.logo")
    opponent_logo2 = serializers.CharField(source="opponent2.logo")
    opponent_name1 = serializers.CharField(source="opponent1.name")
    opponent_name2 = serializers.CharField(source="opponent2.name")
    class Meta:
        model = Fixture
        fields = ('id', 'home_or_away','opponent_name1','opponent_name2','tournament', 'opponent_logo1', 'opponent_logo2','venue','tournament_date','tournament_time','date_created')

class LogSerializer(serializers.ModelSerializer):
    team_logo = serializers.CharField(source="team.logo")
    team_name = serializers.CharField(source="team.name")
    class Meta:
        model = Log
        fields = ('id', 'position', 'team_logo','team_name', 'played', 'won','draws','lost','goal_forward','goal_against','goal_difference','points','date_created')

class ResultSerializer(serializers.ModelSerializer):
    tournament = serializers.CharField(source="tournament.name")
    opponent_logo1= serializers.CharField(source="opponent1.logo")
    opponent_logo2 = serializers.CharField(source="opponent2.logo")
    opponent_name1 = serializers.CharField(source="opponent1.name")
    opponent_name2 = serializers.CharField(source="opponent2.name")
    class Meta:
        model = Result
        fields = ('id', 'tournament', 'opponent_logo1', 'opponent_logo2','opponent_name1','opponent_name2', 'opponent1_score','opponent2_score','venue','time','date_created')