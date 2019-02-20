from rest_framework import serializers
from news.models import News

class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = ('id', 'image', 'heading', 'description', 'date_created')