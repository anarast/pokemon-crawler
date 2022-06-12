from django.contrib import admin

from .models import Pokemon

@admin.register(Pokemon)
class PokemonAdmin(admin.ModelAdmin):
    def get_abilities(self, obj):
        return list(obj.abilities.only('name'))
    
    def get_moves(self, obj):
        return list(obj.moves.only('name'))

    list_display = ('name', 'get_abilities', 'get_moves')
    search_fields = ('name', 'get_abilities', 'get_moves')
    
    get_abilities.short_description = "Abilities"
    get_moves.short_description = "Moves"