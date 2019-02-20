from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import HttpResponse, JsonResponse
from fixtures.models import Fixture,Log,Result
from  .serializers import(
    FixtureSerializer, LogSerializer,
    ResultSerializer,
) 


@api_view(['GET'])
def get_fixtures_list(request):
    if request.method == 'GET':
        fixture = Fixture.objects.all()
        serializer = FixtureSerializer(fixture, many=True)
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_log_list(request):
    if request.method == 'GET':
        log = Log.objects.all()
        serializer = LogSerializer(log, many=True)
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_result_list(request):
    if request.method == 'GET':
        result = Result.objects.all()
        serializer = ResultSerializer(result, many=True)
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)