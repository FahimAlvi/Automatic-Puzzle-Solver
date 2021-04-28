"""
Assignment 2: Automatic Puzzle Solver
==============================
This code is provided solely for the personal and private use of
students taking the CSC148 course at the University of Toronto.
Copying for purposes other than this use is expressly prohibited.
All forms of distribution of this code, whether as given or with
any changes, are expressly prohibited.

=== Module Description ===
This module contains the functions that find solutions to puzzles, step by step.
"""

from __future__ import annotations
from typing import List, Optional, Union, Any
from puzzle import Puzzle

# importing a Queue class to possibly use for breadth_first_solve
from collections import deque

# set higher recursion limit
# which is needed in PuzzleNode.__str__
import sys
sys.setrecursionlimit(10**6)
visited = []

# TODO (Task 8)
# implement depth_first_solve
# do NOT change the type contract
# you are welcome to create any helper functions you like
def depth_first_solve(puzzle: Puzzle) -> Optional[PuzzleNode]:
    """
    Return a path from PuzzleNode(puzzle) to a PuzzleNode containing
    a solution, with each child containing an extension of the puzzle
    in its parent.  Return None if this is not possible.
    """
    global visited
    visited.clear()
    source_node = puzzle_node_builder(puzzle)
    q = deque()
    q.append(source_node)
    visited.remove(source_node.puzzle)
    while q.__len__() != 0:
        v = q.pop()
        child_list = v.children
        for i in child_list:
            if i.puzzle in visited:
                visited.remove(i.puzzle)
                q.appendleft(i)
                i.parent = v
                if i.puzzle.is_solved() is True:
                    return i
    return None





def puzzle_node_builder(p:Puzzle):

    """Creates a puzzle node object from a puzzle object.i.e creates puzzle_nodes"""

    global visited
    if p in visited:
        return None
    if p.extensions() == []:
        return None
    else:
       visited.append(p)
       ext_list = p.extensions()
       children_lst = []
       for i in ext_list:
           print(i)
           temp = puzzle_node_builder(i)
           if temp is not None:
              children_lst.append(temp)
              p_node = PuzzleNode(p, children_lst)
              return p_node



# TODO (Task 9)
# implement breadth_first_solve
# do NOT change the type contract
# you are welcome to create any helper functions you like
# Hint: you may find a queue useful, that's why
#       we imported deque for you above
def breadth_first_solve(puzzle: Puzzle) -> Optional[PuzzleNode]:

    """
    Return a path from PuzzleNode(puzzle) to a PuzzleNode containing
    a solution, with each child PuzzleNode containing an extension
    of the puzzle in its parent.  Return None if this is not possible.
    """

    global visited
    visited.clear()
    source_node = puzzle_node_builder(puzzle)
    q = deque()
    q.appendleft(source_node)
    visited.remove(source_node.puzzle)

    while q.__len__() != 0:
        v = q.popleft()
        child_list = v.children
        for i in child_list:
            # print(i)
            if i.puzzle in visited:
                visited.remove(i.puzzle)
                q.appendleft(i)
                i.parent = v
                if i.puzzle.is_solved() is True:
                    return i
    return None




# The following class has been completed for you
# Do NOT change anything provided in the class below
class PuzzleNode:
    """
    The class PuzzleNode helps build trees of PuzzleNodes that have
    an arbitrary number of children, and a parent.

    === Attributes ===
    puzzle: Optional[Puzzle]
        The configuration (layout) of this puzzle
    children: List[PuzzleNode]
        A list of puzzle nodes that contain puzzles which are extensions (one
        step away) from this puzzle
    parent: Optional[PuzzleNode]
        An optional puzzle node containing a puzzle for which this node's
        puzzle is an extension (one step away) from
    """
    puzzle: Optional[Puzzle]
    children: List[PuzzleNode]
    parent: Optional[PuzzleNode]



    def __init__(self, puzzle: Optional[Puzzle] = None, \
                 children: Optional[List[PuzzleNode]] = None, \
                 parent: Optional[PuzzleNode] = None) -> None:
        """
        Create a new puzzle node self with configuration <puzzle>,
        <children> and <parent>.
        """

        self.puzzle, self.parent = puzzle, parent
        if children is None:
            self.children = []
        else:
            self.children = children[:]








    def __eq__(self, other: Union[PuzzleNode, Any]) -> bool:
        """
        Return whether this PuzzleNode is equivalent to <other>.

        >>> from word_ladder_puzzle import WordLadderPuzzle
        >>> pn1 = PuzzleNode(WordLadderPuzzle("on", "no", {"on", "no", "oo"}))
        >>> pn2 = PuzzleNode(WordLadderPuzzle("on", "no", {"on", "oo", "no"}))
        >>> pn3 = PuzzleNode(WordLadderPuzzle("no", "on", {"on", "no", "oo"}))
        >>> pn1.__eq__(pn2)
        True
        >>> pn1.__eq__(pn3)
        False
        """

        return (type(self) == type(other) and
                self.puzzle == other.puzzle and
                all([x in self.children for x in other.children]) and
                all([x in other.children for x in self.children]))

    def __str__(self) -> str:
        """
        Return a human-readable string representing PuzzleNode self.
        """

        return "{}\n\n{}".format(self.puzzle,
                                 "\n".join([str(x) for x in self.children]))


    """

    Links to websites I used for help in this part of the assignment:

    1)https://www.geeksforgeeks.org/depth-first-search-or-dfs-for-a-graph/

    2)https://eddmann.com/posts/depth-first-search-and-breadth-first-search-in-python/

    3)https://github.com/speix/8-puzzle-solver/blob/master/driver.py?fbclid=IwAR2-mQKxa71I6Lef_9DaapeXUluE9EtZLxq5F1ZNwwzWuxKr_F6kxfLijKA

    4)https://www.youtube.com/watch?v=pcKY4hjDrxk&fbclid=IwAR1GdiuwJSlvx3FY9ikGqqpZ2O7NY7sB7cQs38fborhqjpQnGUjPfL2Co8o

    """

