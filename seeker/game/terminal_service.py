"""
File: terminal_service.py
Authors: Matt Manley (manleym@byui.edu)
         Scott Burton (burtons@byui.edu)
Purpose: The TerminalService class represents the I/O player interface for a
         game of hide and seek.
"""
# class declaration
class TerminalService:
    """A service that handles terminal operations.
    
    The responsibility of a TerminalService is to provide input and output operations for the 
    terminal.
    """

    # method to get player text input and return it to the calling Director 
    def read_text(self, prompt):
        """Gets text input from the terminal. Directs the user with the given prompt.

        Args: 
            self (TerminalService): An instance of TerminalService.
            prompt (string): The prompt to display on the terminal.

        Returns:
            string: The user's input as text.
        """
        return input(prompt)

    # method to get player numerical input and return it to the calling Director
    def read_number(self, prompt):
        """Gets numerical input from the terminal. Directs the user with the given prompt.

        Args: 
            self (TerminalService): An instance of TerminalService.
            prompt (string): The prompt to display on the terminal.

        Returns:
            float: The user's input as a number.
        """
        return float(input(prompt))
        
    # method to simply print text to the screen for the player to read
    def write_text(self, text):
        """Displays the given text on the terminal. 

        Args: 
            self (TerminalService): An instance of TerminalService.
            text (string): The text to display.
        """
        print(text)