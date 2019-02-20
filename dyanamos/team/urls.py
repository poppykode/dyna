from django.urls import path
from .views import (
    current_team,current_team_details,  
)
app_name='team'
urlpatterns = [
    path('current-team/',current_team,name='current-team'),
    path('current-team/<int:pk>',current_team_details,name='current-details'),

]