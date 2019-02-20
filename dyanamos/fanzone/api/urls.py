from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import (
    get_photos_list,get_videos_list,
) 

urlpatterns = [
    path('photos/',  get_photos_list),
    path('videos/', get_videos_list),
]

urlpatterns = format_suffix_patterns(urlpatterns)