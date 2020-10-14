from django.contrib import admin

# Register your models here.

from . models import Genre, Plataform, Game, GameInstance, Developer

admin.site.register(Genre)
admin.site.register(Plataform)
admin.site.register(Game)
admin.site.register(GameInstance)
admin.site.register(Developer)