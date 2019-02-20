from django.urls import path
from .views import (
    news_list,news_detail,
)
app_name='news'
urlpatterns = [
    path('news/',news_list,name='news_list'),
    path('news/<int:pk>',news_detail,name='news_detail'),
]