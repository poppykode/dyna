from rest_framework import serializers
from fanzone.models import (
    Photo,Video,  
) 

class PhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photo
        fields = ('id', 'image','heading','date_created')

class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = ('id', 'cover_image','heading','url','date_created')