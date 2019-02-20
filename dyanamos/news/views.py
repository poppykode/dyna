from django.shortcuts import render,get_object_or_404
from .models import News
from django.core.paginator import Paginator

# Create your views here.

def news_list(request):
    template_name = 'news/news_list.html'
    news = News.objects.all()
    paginator = Paginator(news, 6)

    page = request.GET.get('page')  
    news_list = paginator.get_page(page)

    return render(request,template_name, {'news_list':news_list})

def news_detail(request, pk):
    template_name='news/news_detail.html'
    news= get_object_or_404(News, pk=pk)    
    return render(request, template_name, {'news_detail':news})
