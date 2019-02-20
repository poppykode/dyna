from django.urls import path
from .views import (
    photo_view,video_view,
)
app_name='fanzone'
urlpatterns = [
    path('photos/',photo_view,name='photos'),
    path('videos/',video_view,name='videos'),

]