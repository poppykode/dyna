from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import get_news_list,get_news_by_id

urlpatterns = [
    path('news/', get_news_list),
    path('get_news_by_id/', get_news_by_id),
]

urlpatterns = format_suffix_patterns(urlpatterns)