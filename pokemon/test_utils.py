from pokemon.models import Pokemon

def create_pokemon() -> Pokemon:
  pokemon = Pokemon(name="charmander")
  pokemon.save()
  return pokemon
  
MOCK_POKEMON = [
  {
    "name": "bulbasaur",
    "url": "https://pokeapi.co/api/v2/pokemon/1/"
  },
  {
    "name": "ivysaur",
    "url": "https://pokeapi.co/api/v2/pokemon/2/"
  }
]

MOCK_ABILITIES_1 = [
  {
    "ability": {
      "name": "stance-change",
      "url": "https://pokeapi.co/api/v2/ability/176/"
    },
    "is_hidden": False,
    "slot": 1
  }
]

MOCK_ABILITIES_2 = [
  {
    "ability": {
      "name": "stance-change",
      "url": "https://pokeapi.co/api/v2/ability/176/"
    },
    "is_hidden": False,
    "slot": 1
  },
  {
    "ability": {
      "name": "healer",
      "url": "https://pokeapi.co/api/v2/ability/131/"
    },
    "is_hidden": False,
    "slot": 1
  },
]

