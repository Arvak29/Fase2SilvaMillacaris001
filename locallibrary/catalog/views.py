from django.shortcuts import render
from . models import Genre, Plataform, Developer, User, Game, GameInstance
from django.views import generic

#informacion para formularios
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

#librerias de imagenes
from django.conf.urls import url
from django.shortcuts import render, get_object_or_404
from django.conf import settings
from django.conf.urls.static import static

# Create your views here.
def index(request):
    num_Games = Game.objects.all().count()
    num_Instances = GameInstance.objects.all().count()
    num_instances_available=GameInstance.objects.filter(stock__exact='a').count()
    num_Developer = Developer.objects.count()

    return render(
        request,
        'index.html',
        context={'Num_Games': num_Games, 'Num_Instances': num_Instances, 'num_instances_available':num_instances_available, 'Num_Developer': num_Developer},
    )

def PlaystationStore(request):
    num_Games = Game.objects.all().count()
    num_Instances = GameInstance.objects.all().count()
    num_instances_available=GameInstance.objects.filter(stock__exact='a').count()
    num_Developer = Developer.objects.count()
    '''img = Game.img.objects.all() || , 'Image': img'''

    return render(
        request,
        'PlaystationStore.html',
        context={'Num_Games': num_Games, 'Num_Instances': num_Instances, 'num_instances_available':num_instances_available, 'Num_Developer': num_Developer},
    )


#User CRUD

class UserCreate(CreateView):
    model = User
    fields = ['username', 'password', 'birth_date', 'email']
    initial ={'birth_date': '31/10/2020'}

class UserUpdate(UpdateView):
    model = User
    fields = ['username', 'password', 'birth_date', 'email']

class UserDelete(DeleteView):
    model = User

class UserDetailView(generic.DetailView):
    model = User


#Game CRUD

class GameCreate(CreateView):
    model = Game
    fields = ['title', 'developer', 'description', 'genre', 'plataform', 'players', 'price']

class GameUpdate(UpdateView):
    model = Game
    fields = ['title', 'developer', 'description', 'genre', 'plataform', 'players', 'price']

class GameDelete(DeleteView):
    model = Game

class GameDetailView(generic.DetailView):
    model = Game


#StoreView

class PlataformGameView(generic.DetailView):
    model = Plataform