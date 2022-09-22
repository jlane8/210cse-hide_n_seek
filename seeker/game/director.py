"""
File: director.py
Authors: Matt Manley (manleym@byui.edu)
         Scott Burton (burtons@byui.edu)
Purpose: The Director class represents the game of hide and seek, and all
         direction that happens in it.
"""
# import the other custom classes to create instantiations of the TerminalService,
# Hider, and Seeker objects
from game.terminal_service import TerminalService
from game.hider import Hider
from game.seeker import Seeker

# Director class represents the game and the actions in it
class Director:
    """A person who directs the game. 
    
    The responsibility of a Director is to control the sequence of play.

    Attributes:
        hider (Hider): The game's hider.
        is_playing (boolean): Whether or not to keep playing.
        seeker (Seeker): The game's seeker.
        terminal_service: For getting and displaying information on the terminal.
    """

    # Director constructor
    def __init__(self):
        """Constructs a new Director.
        
        Args:
            self (Director): an instance of Director.
        """
        self._hider = Hider()
        self._is_playing = True
        self._seeker = Seeker()
        self._terminal_service = TerminalService()
        
    # this method runs the game until the hider is found
    def start_game(self):
        """Starts the game by running the main game loop.
        
        Args:
            self (Director): an instance of Director.
        """
        while self._is_playing:
            self._get_inputs()
            self._do_updates()
            self._do_outputs()

    # method to communicate with player through the TerminalService object
    def _get_inputs(self):
        """Moves the seeker to a new location.

        Args:
            self (Director): An instance of Director.
        """
        new_location = self._terminal_service.read_number("\nEnter a location [1-1000]: ")
        self._seeker.move_location(new_location)
        
    # method to update the hider - seeker distance difference
    def _do_updates(self):
        """Keeps watch on where the seeker is moving.

        Args:
            self (Director): An instance of Director.
        """
        self._hider.watch_seeker(self._seeker)
        
    # method to inform player of hints, and to change game control variable if hider is found
    def _do_outputs(self):
        """Provides a hint for the seeker to use.

        Args:
            self (Director): An instance of Director.
        """
        hint = self._hider.get_hint()
        self._terminal_service.write_text(hint)
        if self._hider.is_found():
            self._is_playing = False