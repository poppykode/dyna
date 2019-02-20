from django.shortcuts import render
from django.contrib import messages
from corporate.models import Slider
from news.models import News
from fixtures.models import Fixture
from sponsors.models import Sponsors

# Create your views here.
def home(request):
    sliders = Slider.objects.all()[:3]
    news = News.objects.all()[:4]
    fixtures = Fixture.objects.all()[:3]
    sponsors = Sponsors.objects.all()
    context ={'sliders':sliders,'news':news,'fixtures':fixtures,'sponsors':sponsors}
    return render(request,'corporate/home.html',context)

def about(request):
    return render(request,'corporate/about.html')

def contact(request):
    return render(request,'corporate/contact.html')