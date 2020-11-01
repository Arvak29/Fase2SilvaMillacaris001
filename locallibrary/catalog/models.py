from django.db import models
from django.urls import reverse # Used to generate URLs by reversing the URL patterns
import uuid # Required for unique book instances

# Create your models here.

class Genre (models.Model):

    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Plataform(models.Model):

    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('game-detail', args=[str(self.id)])

class Developer(models.Model):
    name = models.CharField(max_length=100)
    #game = models.ForeignKey('Game', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name

class User(models.Model):
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    birth_date = models.DateField(null=True, blank=True)
    email = models.EmailField(blank=True)

    def get_absolute_url(self):
        return reverse('user_detail', args=[str(self.id)])
    
    def __str__(self):
        return f'{self.username} {self.email}'

class Game(models.Model):

    title = models.CharField(max_length=100)
    developer = models.ManyToManyField(Developer)
    description = models.TextField(max_length=1000, help_text='Enter a brief description of the game')
    genre = models.ManyToManyField(Genre)
    plataform = models.ForeignKey('Plataform', on_delete=models.SET_NULL, null=True)
    players = models.IntegerField(null=True, blank=True)
    price = models.CharField(max_length=9)
    img = models.ImageField(null=True, blank=True, upload_to ='covers')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('game-detail', args=[str(self.id)])

class GameInstance(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text='Unique ID for this particular game across the whole catalog')
    game = models.ForeignKey('Game', on_delete=models.SET_NULL, null=True)
    
    STOCK_STATUS = (
        ('a', 'Available'),
        ('o', 'Out of stock'),
        ('p', 'Pre-order'),
        ('c', 'Coming soon'),
    )

    stock = models.CharField(
        max_length=1,
        choices=STOCK_STATUS,
        blank=True,
        default='a',
        help_text='Game availability',
    )

    def __str__(self):
        return f'{self.id} ({self.game.title})'


