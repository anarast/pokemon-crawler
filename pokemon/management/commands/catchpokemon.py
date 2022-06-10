from django.core.management.base import BaseCommand

from pokemon.pokemon_client import PokemonClient

POKEMON_URL = "https://pokeapi.co/api/v2/pokemon"

class Command(BaseCommand):
    help = 'Catches pokemon and updates their abilities and moves.'

    def handle(self, *args, **options):
      client = PokemonClient(POKEMON_URL)
      client.catch_pokemon()