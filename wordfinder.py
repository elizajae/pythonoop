"""Word Finder: finds random words from a dictionary."""

import random

class WordFinder:
    """
    A class for working with a file of words.
    """

    def __init__(self, file_path):
        """
        Initialize the WordFinder with a file containing words.
        """
        self.file_path = file_path
        self.words = self._read_words_from_file()

    def _read_words_from_file(self):
        """
        Read words from the file and return them as a list.
        """
        try:
            with open(self.file_path, 'r') as file:
                words = [line.strip() for line in file]
                return words
        except FileNotFoundError:
            return []

    def random(self):
        """
        Get a random word from the list of words.
        """
        if self.words:
            return random.choice(self.words)
        else:
            return "No words available"
        
    class SpecialWordFinder(WordFinder):
        """
        A subclass of WordFinder for working with files of words with comments and blank lines.
        """

        def _read_words_from_file(self):
            """
            Read actual words from the file and return them as a list, excluding comments and blank lines.
            """
            try:
                with open(self.file_path, 'r') as file:
                    words = [line.strip() for line in file if line.strip() and not line.startswith("#")]
                    return words
            except FileNotFoundError:
                return []