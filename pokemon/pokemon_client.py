import requests
import logging

from django.core.exceptions import ObjectDoesNotExist

from pokemon.models import Ability, Pokemon, Move

class PokemonClient:
  def __init__(self, url):
    self.url = url
      
  def catch_pokemon(self):
    for pokemon in self.get_pokemon():
      pokemon_name = pokemon['name']
      
      try:
        new_pokemon = Pokemon.objects.get(name=pokemon_name)
        logging.warning(f"Pokemon {str(pokemon)} already exists.")
      except ObjectDoesNotExist:
        new_pokemon = Pokemon(name=pokemon_name)
        new_pokemon.save()
        logging.warning(f"Caught new pokemon {str(pokemon)}")
        
      pokemon_url = pokemon['url']
      
      self.get_and_save_pokemon_details(pokemon=new_pokemon, pokemon_url=pokemon_url)
  
  def get_pokemon(self):
    response = requests.get(self.url)
    pokemon_data = response.json()
    
    while pokemon_data['next'] is not None:
      for pokemon in pokemon_data['results']:
        yield pokemon
      
      response = requests.get(pokemon_data['next'])
      pokemon_data = response.json()
      
  def get_and_save_pokemon_details(self, pokemon: Pokemon, pokemon_url: str):
    response = requests.get(pokemon_url)
    response = response.json()
    self.update_description(pokemon, response['height'], response['weight'])
    self.save_or_update_abilities(pokemon, response['abilities'])
    self.save_or_update_moves(pokemon, response['moves'])
  
  def update_description(self, pokemon: Pokemon, height: int, weight: int):
    pokemon.description = f"A pokemon of height {height} and weight {weight}."
    pokemon.save()
    
  def save_or_update_abilities(self, pokemon: Pokemon, abilities):
    for ability in abilities:
      ability_name = ability['ability']['name']
      
      try:
        new_ability = Ability.objects.get(name=ability_name)
      except ObjectDoesNotExist:
        new_ability = Ability(name=ability_name)
        new_ability.save()
      
      pokemon.abilities.add(new_ability)

  def save_or_update_moves(self, pokemon: Pokemon, moves):
    for move in moves:
      move_name = move['move']['name']
      
      try:
        new_move = Move.objects.get(name=move_name)
      except ObjectDoesNotExist:
        new_move = Move(name=move_name)
        new_move.save()
      
      pokemon.moves.add(new_move)
    