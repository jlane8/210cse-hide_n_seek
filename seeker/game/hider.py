"""
File: hider.py
Authors: Matt Manley (manleym@byui.edu)
         Scott Burton (burtons@byui.edu)
Purpose: The Hider class represents the hider in a game of hide and seek.
"""
# import random module to access random number generation
import random

# Hider class
class Hider:
    """The person hiding from the Seeker. 
    
    The responsibility of Hider is to keep track of its location and 
    distance from the seeker. 
    
    Attributes:
        _location (int): The location of the hider (1-1000).
        _distance (List[int]): The distance from the seeker.
    """

    # constructor for an instantiation of a Hider
    def __init__(self):
        """Constructs a new Hider.

        Args:
            self (Hider): An instance of Hider.
        """
        self._location = random.randint(1, 1000)
        self._distance = [0, 0] # start with two so get_hint always works
    
    # get hint of whether seeker is getting closer or farther away
    def get_hint(self):
        """Gets a hint for the seeker.

        Args:
            self (Hider): An instance of Hider.
        
        Returns:
            string: A hint for the seeker.
        """

        # generate hints
        hint = "(-.-) Nap time."
        if self._distance[-1] == 0:
            hint = f"(;.;) You found me! It took {len(self._distance) - 2} guesses."
        elif self._distance[-1] > self._distance[-2]:
            hint = "(^.^) Getting colder!"
        elif self._distance[-1] < self._distance[-2]:
            hint = "(>.<) Getting warmer!"
        return hint
        
    # method to determine if seeker has found the hider
    def is_found(self):
        """Whether or not the hider has been found.

        Args:
            self (Hider): An instance of Hider.
            
        Returns:
            boolean: True if the hider was found; false if otherwise.
        """
        return (self._distance[-1] == 0)
        
    # method to see how close the seeker currently is
    def watch_seeker(self, seeker):
        """Watches the seeker by keeping track of how far away it is.

        Args:
            self (Hider): An instance of Hider.
        """
        distance = abs(self._location - seeker.get_location())
        self._distance.append(distance)