import mock

from django.test import TestCase

from pokemon.models import Pokemon
from pokemon.pokemon_client import PokemonClient

MOCK_POKEMON = [{
  "name": "bulbasaur",
  "url": "https://pokeapi.co/api/v2/pokemon/1/"
}]

class TestExternalAPI(TestCase):
  def setUp(self):
    self.pokemon_client = PokemonClient("http://example.com")
    
  def test_catch_pokemon(self):
    with mock.patch('pokemon.pokemon_client.PokemonClient.get_pokemon', return_value=MOCK_POKEMON):
      self.pokemon_client.catch_pokemon()
      print(Pokemon.objects.all())
      new_pokemon = Pokemon.objects.latest("id")
      self.assertEquals(new_pokemon.name, "bulbasaur")