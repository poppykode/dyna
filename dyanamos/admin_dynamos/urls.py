from django.urls import path
from .views import (
    fan_of_the_match_list,publish_fan_of_the_match,man_of_the_match_list,
    publish_man_of_the_match,moment_of_the_match_list,publish_moment_of_the_match,
    travel_with_the_team_list,publish_travel_with_the_team,


)
app_name='admin_dynamos'
urlpatterns = [
    path('fan_of_the_match/',fan_of_the_match_list,name='ftm'),
    path('publish/fan_of_the_match/<int:pk>/',publish_fan_of_the_match, name='fan_of_the_match'),
    path('man_of_the_match/',man_of_the_match_list,name='mtm'),
    path('publish/man_of_the_match/<int:pk>/',publish_man_of_the_match, name='man_of_the_match'),
    path('moment_of_the_match/',moment_of_the_match_list,name='motm'),
    path('publish/moment_of_the_match/<int:pk>/',publish_moment_of_the_match, name='moment_of_the_match'),
    path('travel_with_the_team/',travel_with_the_team_list,name='ttt'),
    path('publish/travel_with_the_team/<int:pk>/',publish_travel_with_the_team, name='travel_with_the_team'),
    
]