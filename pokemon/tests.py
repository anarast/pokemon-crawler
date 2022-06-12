import mock

from django.test import TestCase

from pokemon.models import Pokemon
from pokemon.pokemon_client import PokemonClient
from pokemon.test_utils import MOCK_POKEMON, MOCK_ABILITIES_1, MOCK_ABILITIES_2, create_pokemon

class TestExternalAPI(TestCase):
  def setUp(self):
    self.pokemon_client = PokemonClient("http://example.com")
  
  def test_catch_pokemon(self):
    with mock.patch('pokemon.pokemon_client.PokemonClient.get_pokemon', return_value=MOCK_POKEMON):
      # Check that the correct number of pokemon were created.
      self.pokemon_client.catch_pokemon()
      self.assertEqual(len(MOCK_POKEMON), Pokemon.objects.count())
      
      # Check that the correct pokemon were created.
      bulbasaur = Pokemon.objects.get(name="bulbasaur")
      self.assertIsNotNone(bulbasaur)
      ivysaur = Pokemon.objects.get(name="ivysaur")
      self.assertIsNotNone(ivysaur)
      
  def test_update_description(self):
    pokemon = create_pokemon()
    height = 55
    weight = 155
    self.pokemon_client.update_description(pokemon, height, weight)
    pokemon.refresh_from_db()
    expected_description = f"A pokemon of height {height} and weight {weight}."
    self.assertEqual(pokemon.description, expected_description)
    
  def test_save_ability(self):
    pokemon = create_pokemon()
    self.pokemon_client.save_or_update_abilities(pokemon, MOCK_ABILITIES_1)
    self.assertTrue(pokemon.abilities.filter(name="stance-change").exists())
    
  def test_update_ability(self):
    pokemon = create_pokemon()
    self.pokemon_client.save_or_update_abilities(pokemon, MOCK_ABILITIES_1)
    self.pokemon_client.save_or_update_abilities(pokemon, MOCK_ABILITIES_2)

    self.assertTrue(pokemon.abilities.filter(name="stance-change").exists())
    self.assertTrue(pokemon.abilities.filter(name="healer").exists())