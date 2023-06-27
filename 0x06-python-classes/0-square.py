#!/usr/bin/python3

class Square:
    """A class representing a square.

    This class provides methods to calculate the area and perimeter
    of a square.

    Attributes:
        side_length (int): The length of each side of the square.
    """

    def __init__(self, side_length):
        """Initialize a square object with a given side length.

        Args:
            side_length (int): The length of each side of the square.
        """
        self.side_length = side_length

    def calculate_area(self):
        """Calculate the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.side_length ** 2

    def calculate_perimeter(self):
        """Calculate the perimeter of the square.

        Returns:
            int: The perimeter of the square.
        """
        return 4 * self.side_length
