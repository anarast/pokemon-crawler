from django.db import models

class Ability(models.Model):
    name = models.CharField(max_length=50, unique=True)
    
    def __str__(self):
        return self.name

class Move(models.Model):
    name = models.CharField(max_length=50, unique=True)
    
    def __str__(self):
        return self.name
      
class Pokemon(models.Model):
    name = models.CharField(max_length=50, unique=True)
    description = models.CharField(max_length=200)
    abilities = models.ManyToManyField(Ability)
    moves = models.ManyToManyField(Move)
    
    def __str__(self):
        return self.name