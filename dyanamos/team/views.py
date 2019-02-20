from django.shortcuts import render,get_object_or_404
from .models import CurrentTeam

# Create your views here.
def current_team(request):
    template_name = 'team/current_team.html'
    all_players = CurrentTeam.objects.all()
    goalkeepers = CurrentTeam.objects.filter(position='Goalkeeper')
    forwards = CurrentTeam.objects.filter(position='Forward')
    midfielders = CurrentTeam.objects.filter(position='Midfielder')
    defenders = CurrentTeam.objects.filter(position='Defender')
    context ={'all_players':all_players,'goalkeepers':goalkeepers,'forwards':forwards,'midfielders':midfielders,'defenders':defenders}
    return render(request,template_name,context)

def current_team_details(request,pk):
    template_name='team/current_team_details.html'
    current_team= get_object_or_404(CurrentTeam, pk=pk)  
    return render(request,template_name,{'current_team':current_team})




