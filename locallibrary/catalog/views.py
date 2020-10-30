from django.shortcuts import render
from . models import Genre, Plataform, Developer, Game, GameInstance
from django.views import generic

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

    return render(
        request,
        'PlaystationStore.html',
        context={'Num_Games': num_Games, 'Num_Instances': num_Instances, 'num_instances_available':num_instances_available, 'Num_Developer': num_Developer},
    )
