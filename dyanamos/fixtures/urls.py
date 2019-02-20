from django.urls import path
from .views import (
    match_result_view,log_view,Fixture,
    fixtures_view,
    
)
app_name='fixtures'
urlpatterns = [
    path('results/',match_result_view, name='results'),
    path('log/',log_view, name='log'),
    path('fixtures/',fixtures_view, name='fixtures'),

]