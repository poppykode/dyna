from django.shortcuts import render
from django.shortcuts import render,get_object_or_404
from django.core.paginator import Paginator
from .models import (
    Result,Log, Fixture,
)

# Create your views here.
def match_result_view(request):
    template_name = 'fixtures/result_list.html'
    results_list = Result.objects.all()
    paginator = Paginator(results_list,2)
    page = request.GET.get('page')
    results = paginator.get_page(page)
    return render(request,template_name,{'results':results})

def log_view(request):
    template_name = 'fixtures/log_result_list.html'
    log_results = Log.objects.all()
    return render(request,template_name,{'log_results':log_results})

def fixtures_view(request):
    template_name = 'fixtures/fixtures_list.html'
    fixture_list = Fixture.objects.all()
    paginator = Paginator(fixture_list, 2)
    page = request.GET.get('page')
    fixture = paginator.get_page(page)
    return render(request,template_name,{'fixtures':fixture})


    



