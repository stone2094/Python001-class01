from django.shortcuts import render
from .models import Movies
from .models import T1
# Create your views here.

from django.http import HttpResponse
def index(request):
    return HttpResponse("Hello Django!")

'''
def movies(request):
    ###  从models取数据传给template  ###
    m = Movies.objects.all()
    return render(request, 'movies.html', locals())
'''
def movies(request):
    ###  从models取数据传给template  ###
    movieslist = T1.objects.all()
    # 评论数量
    counter = T1.objects.all().count()

    queryset = T1.objects.values('stars')
    condtions = {'stars__gte': 0.5}
    plus = queryset.filter(**condtions).count()

    return render(request, 'movies.html', locals())