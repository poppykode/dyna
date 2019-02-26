from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from rest_framework.decorators import api_view
from django.core.paginator import Paginator
from accounts.models import (
    FanOfTheMatch,ManOfTheMatch,
    TravelWithTheTeam,MomementOfTheMatch,
)
from accounts.forms import (
    FanOfTheMatchForm,ManOfTheMatchForm,TravelWithTheTeamForm,
    MomementOfTheMatchForm,
)

# Create your views here.
def fan_of_the_match_list(request):
    template_name = 'admin_dynamos/fan_of_the_match_list.html'
    ftm_list = FanOfTheMatch.objects.all()
    paginator = Paginator(ftm_list, 10)

    page = request.GET.get('page')  
    ftm = paginator.get_page(page)
    return render(request,template_name,{'ftm':ftm})

def publish_fan_of_the_match(request,pk):
    template_name = 'admin_dynamos/publish_fan_of_the_match.html' 
    ftm = get_object_or_404(FanOfTheMatch, pk=pk)
    if request.method =='POST':
        form = FanOfTheMatchForm(request.POST,request.FILES,instance=ftm)
        if form.is_valid():                          
            form.save()
            messages.success(request, 'post has been published')
            return redirect('admin_dynamos:ftm')#missing
    else:     
        context = {'form': FanOfTheMatchForm(instance=ftm)}
    return render(request,template_name,context)

def man_of_the_match_list(request):
    template_name = 'admin_dynamos/man_of_the_match_list.html'
    mtm_list = ManOfTheMatch.objects.all()
    paginator = Paginator(mtm_list, 10)

    page = request.GET.get('page')  
    mtm = paginator.get_page(page)
    return render(request,template_name,{'mtm_list':mtm})

def publish_man_of_the_match(request,pk):
    template_name = 'admin_dynamos/publish_man_of_the_match.html' 
    mtm= get_object_or_404(ManOfTheMatch, pk=pk)
    if request.method =='POST':
        form = ManOfTheMatchForm(request.POST,request.FILES,instance=mtm)
        if form.is_valid():                          
            form.save()
            messages.success(request, 'post has been published')
            return redirect('admin_dynamos:mtm')
    else:     
        context = {'form': ManOfTheMatchForm(instance=mtm)}
    return render(request,template_name,context)


def moment_of_the_match_list(request):
    template_name = 'admin_dynamos/moment_of_the_match_list.html'
    motm_list = MomementOfTheMatch.objects.all()
    paginator = Paginator(motm_list, 10)
    page = request.GET.get('page')  
    motm = paginator.get_page(page)
    return render(request,template_name,{'motm':motm})

def publish_moment_of_the_match(request,pk):
    template_name = 'admin_dynamos/publish_moment_of_the_match.html'
    motm= get_object_or_404(MomementOfTheMatch,pk=pk)
    if request.method =='POST':
        form = MomementOfTheMatchForm(request.POST,request.FILES,instance=motm)
        if form.is_valid():                          
            form.save()
            messages.success(request, 'post has been published')
            return redirect('admin_dynamos:motm')#mising
    else:     
        context = {'form': MomementOfTheMatchForm(instance=motm)}
    return render(request,template_name,context)

def travel_with_the_team_list(request):
    template_name = 'admin_dynamos/travel_with_the_team_list.html'
    ttt_list = TravelWithTheTeam.objects.all()
    paginator = Paginator(ttt_list, 10)
    page = request.GET.get('page')  
    ttt = paginator.get_page(page)
    return render(request,template_name,{'ttt':ttt})

def publish_travel_with_the_team(request,pk):
    template_name = 'admin_dynamos/publish_travel_with_the_team.html'
    ttt= get_object_or_404(TravelWithTheTeam,pk=pk)
    if request.method =='POST':
        form = TravelWithTheTeamForm(request.POST,request.FILES,instance=ttt)
        if form.is_valid():                          
            form.save()
            messages.success(request, 'post has been published')
            return redirect('admin_dynamos:ttt')
    else:     
        context = {'form': TravelWithTheTeamForm(instance=ttt)}
    return render(request,template_name,context)