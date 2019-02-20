from django.urls import path
from .views import (
    membership_profile,register,fan_of_the_match,
    man_of_the_match,moment_of_the_match,travel_with_the_team,
    loyalty,loyalty_points,
)
app_name='accounts'
urlpatterns = [
    path('register/', register,name='register'),
    path('profile/', membership_profile,name='profile'),
    path('fan-of-the-match/', fan_of_the_match,name='ftm'),
    path('man-of-the-match/', man_of_the_match,name='mtm'),
    path('moment-of-the-match/', moment_of_the_match,name='motm'),
    path('travel-with-the-team/', travel_with_the_team,name='ttt'),
    path('loyalty/', loyalty,name='loyalty'),
    path('loyalty-=points/', loyalty_points,name='loyalty_points'),
]