from django.shortcuts import render,redirect
from .models import Photo,Video
from django.db.models import F
from accounts.models import (
    FanOfTheMatch,ManOfTheMatch,
    TravelWithTheTeam,MomementOfTheMatch,
)
from django.core.paginator import Paginator
from django.contrib import messages


# Create your views here.
def photo_view(request):
    template_name = 'fanzone/photos_list.html'
    photos_list = Photo.objects.all()
    paginator = Paginator(photos_list,8) # Show 25 contacts per page

    page = request.GET.get('page')
    photos = paginator.get_page(page)
    return render(request,template_name,{'photos':photos})

def video_view(request):
    template_name = 'fanzone/videos_list.html'
    videos_list = Video.objects.all()
    paginator = Paginator(videos_list,4) # Show 25 contacts per page

    page = request.GET.get('page')
    videos = paginator.get_page(page)
    return render(request,template_name,{'videos':videos})

def voting_view(request):
    template_name = 'fanzone/voting.html'
    mtm = ManOfTheMatch.objects.filter(published=True)
    ftm = FanOfTheMatch.objects.filter(published=True)
    motm = MomementOfTheMatch.objects.filter(published=True)
    ttt = TravelWithTheTeam.objects.filter(published=True)

    return render(request,template_name,{'mtm':mtm,'ftm':ftm,'motm':motm,'ttt':ttt})


def man_of_the_match_votes(requests,mtm_id):
    mtm = ManOfTheMatch.objects.get(id=mtm_id)
    mtm.votes = F('votes') + 1
    mtm.save()
    print(mtm.votes)
    mtm.refresh_from_db()
    print(mtm.votes) 
    new_vote =  mtm.votes
    messages.success(requests, 'Thank you for voting.')
    return redirect('fanzone:voting')

def fan_of_the_match_votes(requests,fan_id):
    fan = FanOfTheMatch.objects.get(id=fan_id)
    fan.votes = F('votes') + 1
    fan.save()
    print(fan.votes)
    fan.refresh_from_db()
    print(fan.votes) 
    new_vote =  fan.votes
    messages.success(requests, 'Thank you for voting.')
    return redirect('fanzone:voting')

def moment_of_the_match_votes(requests,momt_id):
    momt = MomementOfTheMatch.objects.get(id=momt_id)
    momt.votes = F('votes') + 1
    momt.save()
    print(momt.votes)
    momt.refresh_from_db()
    print(momt.votes) 
    new_vote =  momt.votes
    messages.success(requests, 'Thank you for voting.')
    return redirect('fanzone:voting')

def travel_with_the_team_votes(requests,ttt_id):
    ttt = TravelWithTheTeam.objects.get(id=ttt_id)
    ttt.votes = F('votes') + 1
    ttt.save()
    print(ttt.votes)
    ttt.refresh_from_db()
    print(ttt.votes) 
    new_vote = ttt.votes
    messages.success(requests, 'Thank you for voting.')
    return redirect('fanzone:voting')



