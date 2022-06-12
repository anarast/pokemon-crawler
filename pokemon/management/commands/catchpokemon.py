import traceback

from django.core.management.base import BaseCommand

from pokemon.pokemon_client import PokemonClient
from pokemon.constants import POKEMON_URL

class Command(BaseCommand):
  help = 'Catches pokemon and updates their abilities and moves.'

  def handle(self, *args, **options):
    try:
      client = PokemonClient(POKEMON_URL)
      client.catch_pokemon()
    except:
      traceback.print_exc()
