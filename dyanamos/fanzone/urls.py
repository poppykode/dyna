from django.urls import path
from .views import (
    photo_view,video_view,voting_view,
    man_of_the_match_votes,fan_of_the_match_votes,
    moment_of_the_match_votes,travel_with_the_team_votes,
)
app_name='fanzone'
urlpatterns = [
    path('photos/',photo_view,name='photos'),
    path('videos/',video_view,name='videos'),
    path('voting/',voting_view,name='voting'),
    path('man_of_the_match_votes/<int:mtm_id>/',man_of_the_match_votes,name='mtm'), 
    path('fan_of_the_match_votes/<int:fan_id>/',fan_of_the_match_votes,name='fan'), 
    path('moment_of_the_match_votes/<int:momt_id>/',moment_of_the_match_votes,name='momt'),
    path('travel_with_the_team_votes/<int:ttt_id>/',travel_with_the_team_votes,name='ttt'),  
]