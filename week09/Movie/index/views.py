from django.shortcuts import render,redirect
from .models import Movies
from .models import T1
from .form import LoginForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
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

def wrong_password(request):
  return render(request, 'wrong_password.html')


@login_required(login_url='/')
def logged_in(request):
  #return render(request, 'movies.html')
  return render(request, 'logged_in.html')


def login2(request):
  if request.method == 'POST':
    login_form = LoginForm(request.POST)
    if login_form.is_valid():
      cd = login_form.cleaned_data
      user = authenticate(username=cd['username'], password=cd['password'])
      if user:
        login(request, user)
        return redirect('/logged_in')
      else:
        return redirect('/wrong_password')
  if request.method == "GET":
    login_form = LoginForm()
    return render(request, 'form.html', {'form': login_form})