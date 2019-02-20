
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import HttpResponse, JsonResponse
from team.models import CurrentTeam
from .serializers import CurrentTeamSerializer


@api_view(['GET'])
def get_current_team_list(request):
    if request.method == 'GET':
        ct = CurrentTeam.objects.all()
        serializer = CurrentTeamSerializer(ct, many=True)
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET',])
def get_current_team_by_id(request):
    if request.method == 'GET':
        queryset = CurrentTeam.objects.all()
        id = request.query_params.get('id', None)
        if id is not None:
            queryset = queryset.filter(id=id)    
            serializer = CurrentTeamSerializer(queryset ,many=True)
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
