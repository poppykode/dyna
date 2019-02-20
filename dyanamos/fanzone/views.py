from django.shortcuts import render
from .models import Photo,Video
from django.core.paginator import Paginator


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

