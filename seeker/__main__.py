"""
File: __main__.py
Authors: Matt Manley (manleym@byui.edu)
         Scott Burton (burtons@byui.edu)
Purpose: This is the entry point into the hide and seek game.
"""
# import the Director class to create an instantiation of Director 
from game.director import Director

# create instantiation of Director and start the game
director = Director()
director.start_game()