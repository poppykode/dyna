from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import (
    get_current_team_list,get_current_team_by_id,

) 

urlpatterns = [
    path('players/', get_current_team_list),
    path('get_player_by_id/', get_current_team_by_id),
]

urlpatterns = format_suffix_patterns(urlpatterns)