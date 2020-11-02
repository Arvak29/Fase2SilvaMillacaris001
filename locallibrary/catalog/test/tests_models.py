from django.test import TestCase
from catalog.models import Game, Plataform

class YourTestClass(TestCase):

    def setUp(self):
        a1=Plataform.objects.create(name="Playstation 4")
        Game.objects.create(title="Monster Hunter World", plataform=a1)

    def test_games_plataform(self):
        game1 = Game.objects.get(title="Monster Hunter World")
        self.assertEqual(game1.plataform.name, "Playstation 4")
        
