from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import HttpResponse, JsonResponse
from news.models import News
from .serializers import NewsSerializer


@api_view(['GET'])
def get_news_list(request):
    if request.method == 'GET':
        news = News.objects.all()
        serializer = NewsSerializer(news, many=True)
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET',])
def get_news_by_id(request):
    if request.method == 'GET':
        queryset = News.objects.all()
        id = request.query_params.get('id', None)
        if id is not None:
            queryset = queryset.filter(id=id)    
            serializer = NewsSerializer(queryset ,many=True)
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
