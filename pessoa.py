# -*- coding: utf-8 -*-
import random

from pokemon import *

NOMES = [
            "João", "Isabela", "Lorena", "Francisco", "Ricardo", "Diego", 
            "Patrícia", "Marcelo", "Gary"
        ]


class Pessoa:
   
    def __init__(self, nome=None, pokemons=[]):
        if nome:
            self.nome = nome 
        else:
            self.nome = random.choice(NOMES)

        self.pokemons = pokemons

    def __str__(self):
        return self.nome

    def mostrar_pokemons(self):
        if self.pokemons:
            print("Pokemons de {}:".format(self))
            for pokemon in self.pokemons:
                print(pokemon)
        else:
            print("{} não têm nenhum pokemon".format(self))

class Player(Pessoa):
    tipo = "player"

    def capturar(self, pokemon):
        self.pokemons.append(pokemon)
        print("{} capturou {}".format(self, pokemon))


class Inimigo(Pessoa):
    tipo = "inimigo"


eu = Player()

print(eu)
