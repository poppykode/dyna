from django.shortcuts import render,redirect
from django.urls import reverse
from django.contrib import messages
from fixtures.models import Fixture
from .models import Loyalty
from news.models import News
from accounts.models import User
from django.db import IntegrityError
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import (
    SignUpForm,FanOfTheMatchForm,
    ManOfTheMatchForm,TravelWithTheTeamForm,
    MomementOfTheMatchForm,
)
import datetime
from django.utils import timezone
 

# Create your views here.

def register(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Registration has completed successfully.')
            return redirect(reverse('login'))
    else:
        form = SignUpForm()    
    return render(request,'registration/register.html',{'form':form})

@login_required
def membership_profile(request):
    news = News.objects.all()[:3]
    loggedin_user = User.objects.filter(id=request.user.id)
    return render(request,'registration/profile.html',{'news':news})

def calculate_points(request):
    points = Loyalty.objects.filter(user=request.user)
    pt = 0
    for x in points:
        pt += x.points  
    return pt

def forlife(total_points):
    forlife=[]
    if total_points < 50:
        forlife='OG Forlife'
        return forlife
    elif total_points < 75:
        forlife='VIP Forlife'
        return forlife
    else:
        forlife='VVIP ForlIfe'
        return forlife


@login_required
def loyalty(request):
    print(datetime.date.today())
    fixture = Fixture.objects.filter(tournament_date=datetime.date.today())[:1]
    total_points = calculate_points(request)
    lyf = forlife(total_points)
    print(lyf)
    return render(request,'registration/loyalty.html',{'fixtures':fixture,'points':total_points,'forlyf':lyf})

@login_required
def loyalty_points(request):
    if request.method == 'POST':
        venue = request.POST.get("venue")
        tournament_date = request.POST.get("tournament_date")
        teams_played = request.POST.get("teams_played")
        current_user = request.user
        points = 5
        try:
            Loyalty.objects.create(
                venue = venue,
                tournament_date = str(tournament_date),
                teams_played = teams_played,
                user = current_user,
                points =points,
            )
            messages.success(request, 'Thanks for endorsing!')
            return redirect('accounts:loyalty')
        except IntegrityError as e:
            messages.error(request, 'You have already endorsed the game.')
            return redirect('accounts:loyalty')

@login_required
def fan_of_the_match(request):
    if request.user.sub_expiration_date < timezone.now():
        messages.error(request, 'Please makepayment!')
        return redirect('subs:make-payment-subscribe') 
    else:   
        if request.method == 'POST':
            form= FanOfTheMatchForm(request.POST,request.FILES)
            if form.is_valid():
                new_form = form.save(commit=False)
                new_form.user = request.user
                form.save()
                print(request.user.paid)
                messages.success(request, 'image has been successfully uploaded now waiting Admin approval!')
                return redirect('accounts:ftm')
        else:
            form= FanOfTheMatchForm()
        return render(request,'registration/fan_of_the_match.html',{'form':form })

@login_required
def man_of_the_match(request):
    if request.user.sub_expiration_date < timezone.now():
        messages.error(request, 'Please makepayment!')
        return redirect('subs:make-payment-subscribe')
    else:
        if request.method == 'POST':
            form= ManOfTheMatchForm(request.POST,request.FILES)
            if form.is_valid():
                new_form = form.save(commit=False)
                new_form.user = request.user
                form.save()
                messages.success(request, 'image has been successfully uploaded now waiting Admin approval!')
                return redirect('accounts:mtm')
        else:
            form= ManOfTheMatchForm()
        return render(request,'registration/man_of_the_match.html',{'form':form })
  
@login_required
def travel_with_the_team(request):
    if request.user.sub_expiration_date < timezone.now():
        messages.error(request, 'Please makepayment!')
        return redirect('subs:make-payment-subscribe')
    else:
        if request.method == 'POST':
            form= TravelWithTheTeamForm(request.POST,request.FILES)
            if form.is_valid():
                new_form = form.save(commit=False)
                new_form.user = request.user
                form.save()
                messages.success(request, 'image has been successfully uploaded now waiting Admin approval!')
                return redirect('accounts:ttt')
        else:
            form= TravelWithTheTeamForm()
        return render(request,'registration/travel_with_the_team.html',{'form':form })

@login_required      
def moment_of_the_match(request):
    if request.user.sub_expiration_date > timezone.now():
        messages.error(request, 'Please makepayment!')
        return redirect('subs:make-payment-subscribe')
    else:
        if request.method == 'POST':
            form= MomementOfTheMatchForm(request.POST,request.FILES)
            if form.is_valid():
                new_form = form.save(commit=False)
                new_form.user = request.user
                form.save()
                messages.success(request, 'image has been successfully uploaded now waiting Admin approval!')
                return redirect('accounts:motm')
        else:
            form= MomementOfTheMatchForm()
        return render(request,'registration/moment_of_the_match.html',{'form':form})

    

