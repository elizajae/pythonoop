"""Python serial number generator."""

class SerialGenerator:
    """Machine to create unique incrementing serial numbers.
    
    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """
    def __init__(self, start):
        """
        Initialize the SerialGenerator with a start number.

        Args:
        - start (int): The starting number.
        """
        self.start = start
        self.current = start

    def generate(self):
        """
        Get the next sequential number.

        Returns:
        int: The next sequential number.
        """
        result = self.current
        self.current += 1
        return result

    def reset(self):
        """
        Reset the number to the starting value.
        """
        self.current = self.start
