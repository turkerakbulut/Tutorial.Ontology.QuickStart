#
# Türker Akbulut 2020
#
# https://owlready2.readthedocs.io/en/latest/onto.html#creating-an-ontology

from owlready2 import *
import os

# Working directory
directory = os.path.dirname(__file__)
# Onto path append
onto_path.append(directory + "/Repo")
# Ontology load
onto = get_ontology(directory + "/Repo/game.owl").load()

########
print(onto.Masters.is_a)
print(onto.Tennis.is_a)
print(onto.Grass.is_a)
print(onto.Surface.is_a)
print(onto.RacquetGames.is_a)
print(onto.Game.is_a)
print(onto.ITFFeature.is_a)
print(onto.search_one(is_a=onto.Masters))
print(onto.RogerFederer.is_a)
print(onto.Player.is_a)
print(list(onto.classes()))
print(list(onto.properties()))
print(list(onto.individuals()))
