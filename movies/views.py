from django.http import HttpResponse
from django.template import loader
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from .models import movies
from .models import user
from movies.forms import moviesForm, userForm

def index(request):
    movies = movies.objects.all()
    user = user.objects.all()
    
    context = {
        'movies': movies,
        'user': user,
    }
    
    template = loader.get_template('index.html')
    return HttpResponse(template.render(context, request))

def movies(request, movies_id):
    movies = movies.objects.get(id=movies_id)
    template = loader.get_template('display_movie.html')
    context = {
        'movies': movies
    }
    return HttpResponse(template.render(context, request))

def user(request, user_id):
    user_id = user.objects.get(id=user_id)
    template = loader.get_template('display_trainer.html')
    context = {
        'user': user
    }
    return HttpResponse(template.render(context, request))

@login_required
def add_movies(request):
    if request.method == 'POST':
        form = moviesForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('movies:index')
    else:
        form = moviesForm()
    
    return render(request, 'movies_form.html', {'form': form})

def edit_movies(request, movies_id):
    movies = movies.objects.get(id=movies_id)
    if request.method == 'POST':
        form = moviesForm(request.POST, request.FILES, instance=movies)
        if form.is_valid():
            form.save()
            return redirect('movies:index')
    else:
        form = moviesForm(instance=movies)
    
    return render(request, 'movies_form.html', {'form': form})

def delete_movies(request, movies_id):
    movies = movies.objects.get(id=movies_id)
    movies.delete()
    return redirect('movies:index')

def add_user(request):
    if request.method == 'POST':
        form = userForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('movies:index')
    else:
        form = userForm()
    
    return render(request, 'user_form.html', {'form': form})

def edit_user(request, user_id):
    user = user.objects.get(id=user_id)
    if request.method == 'POST':
        form = userForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            return redirect('mocies:index')
    else:
        form = userForm(instance=user)
    
    return render(request, 'user_form.html', {'form': form})

def delete_user(request, user_id):
    user = user.objects.get(id=user_id)
    user.delete()
    return redirect('movies:index')

class CustomLoginView(LoginView):
    template_name = "login_form.html"