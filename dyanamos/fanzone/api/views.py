
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import HttpResponse, JsonResponse
from fanzone.models import Photo,Video
from .serializers import PhotoSerializer,VideoSerializer


@api_view(['GET'])
def get_photos_list(request):
    if request.method == 'GET':
        photo = Photo.objects.all()
        serializer = PhotoSerializer(photo, many=True)
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_videos_list(request):
    if request.method == 'GET':
        vids = Video.objects.all()
        serializer = VideoSerializer(vids, many=True)
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)