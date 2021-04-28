"""
Assignment 2: Automatic Puzzle Solver
==============================
This code is provided solely for the personal and private use of
students taking the CSC148 course at the University of Toronto.
Copying for purposes other than this use is expressly prohibited.
All forms of distribution of this code, whether as given or with
any changes, are expressly prohibited.

=== Module Description ===
This module contains the class required to solve word ladder puzzles.
"""

from __future__ import annotations
from typing import Set
from puzzle import Puzzle

class WordLadderPuzzle(Puzzle):
    """
    A word-ladder puzzle that may be solved, unsolved, or even unsolvable.
    """

    def __init__(self, from_word: str, to_word: str, ws: Set[str]) -> None:
        """
        Create a new word-ladder puzzle with the aim of stepping
        from from_word to to_word using words in ws, changing one
        character at each step.
        """
        # Private Attributes
        # _from_word
        #   the initial word the puzzle begins with
        # _to_word
        #   the goal word the puzzle wants to change to
        # _word_set
        #   the set of all words that are possible valid words to change into
        # _chars
        #   a string of all possible characters that a word may consist of

        _from_word: str
        _to_word: str
        _word_set: Set[str]
        _chars: str

        (self._from_word, self._to_word, self._word_set) = (from_word,
                                                            to_word, ws)
        # set of characters to use for 1-character changes
        self._chars = "abcdefghijklmnopqrstuvwxyz"

    # TODO (Task 4)
    # implement __eq__ and __str__
    # __repr__ is optional / up to you

    def __eq__(self, other:WordLadderPuzzle) -> bool:
        return (type(other) == type(self) and self._from_word == other._from_word and self._to_word == other._to_word)

    def __str__(self) -> str:
        s="{0} -> {1}"
        return(s.format(self._from_word,self._to_word))




    # TODO (Task 5)
    # override extensions
    # legal extensions are WordLadderPuzzles that have a from_word that can
    # be reached from this one by changing a single letter to one of those
    # in self._chars
    def extensions(self):
        ext_list = []
        for i in range(len(self._to_word)):
            x = self._to_word[i]
            from_word_list = list(self._from_word)
            from_word_list[i] = x
            new_word = self.list_to_str(from_word_list)
            if new_word in self._word_set:
                new_game = WordLadderPuzzle(new_word, self._to_word, self._word_set)
                ext_list.append(new_game)
        return ext_list

    #helper
    def list_to_str(self,l:list):
        """Converts a List to a string"""
        s = ""
        for i in l:
            s += i
        return s

    # TODO (Task 5)
    # override is_solved
    # Note: this WordLadderPuzzle is solved when _from_word is the same as
    # _to_word

    def is_solved(self):
        return (self._from_word == self._to_word)


if __name__ == '__main__':
    import doctest
    doctest.testmod()

    # Comment out the code below as you solve necessary parts of the assignment
    from puzzle_tools import breadth_first_solve, depth_first_solve
    from time import time
    with open("words", "r") as words:
        word_set = set(words.read().split())
    w = WordLadderPuzzle("same", "cost", word_set)

    start = time()
    sol = breadth_first_solve(w)
    end = time()
    print("Solving word ladder from same->cost")
    print("...using breadth-first-search")
    print("Solutions: {} took {} seconds.".format(sol, end - start))
    start = time()
    sol = depth_first_solve(w)
    end = time()
    print("Solving word ladder from same->cost")
    print("...using depth-first-search")
    print("Solutions: {} took {} seconds.".format(sol, end - start))

