from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import (
    get_fixtures_list,get_log_list,
    get_result_list,
) 

urlpatterns = [
    path('fixtures/', get_fixtures_list),
    path('log/', get_log_list),
    path('results/', get_result_list),
]

urlpatterns = format_suffix_patterns(urlpatterns)