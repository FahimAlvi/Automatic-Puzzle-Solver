"""
Assignment 2: Automatic Puzzle Solver
==============================
This code is provided solely for the personal and private use of
students taking the CSC148 course at the University of Toronto.
Copying for purposes other than this use is expressly prohibited.
All forms of distribution of this code, whether as given or with
any changes, are expressly prohibited.

=== Module Description ===
This module contains the class required to solve grid peg solitaire puzzles.
"""
from __future__ import annotations
from typing import List, Set
from puzzle import Puzzle

class GridPegSolitairePuzzle(Puzzle):
    """
    Snapshot of peg solitaire on a rectangular grid. May be solved,
    unsolved, or even unsolvable.
    """

    def __init__(self, marker: List[List[str]], marker_set: Set[str]):
        """
        Create a new GridPegSolitairePuzzle self with
        marker indicating pegs, spaces, and unused
        and marker_set indicating allowed markers.

        Note: The symbol "#" is for unused, "*" is for peg, "." is for empty

        Precondition:
        - marker is a non-empty list of lists representing an m x n grid
        - the strings in marker are all a valid string from marker_set
        """
        # Private Attributes
        # _marker
        #   the m x n solitaire grid with some pegs, spaces and unused spots
        # _marker_set
        #   the possible symbols on the grid, representing different spots

        _marker: str
        _marker_set: str


        self._marker, self._marker_set = marker, marker_set

    # TODO (Task 2)
    # implement __eq__ and __str__
    # __repr__ is optional / up to you

    def __eq__(self, other:GridPegSolitairePuzzle) -> bool:
        """
        >>> grid1 = [["*", "*", "*", "*", "*"],\
        ["*", "*", "*", "*", "*"],\
        ["*", "*", "*", "*", "*"],\
        ["*", "*", ".", "*", "*"],\
        ["*", "*", "*", "*", "*"]]
        >>> grid2 =[["*", "*", "*", "*", "*"],\
        ["*", "*", "*", "*", "*"],\
        ["*", "*", "*", "*", "*"],\
        ["*", "*", ".", "*", "*"],\
        ["*", "*", "*", "*", "*"]]
        >>> g1=GridPegSolitairePuzzle(grid1,{"*", ".", "#"})
        >>> g2=GridPegSolitairePuzzle(grid2,{"*", ".", "#"})
        >>> g1.__eq__(g2)
        True
        """
        if len(self._marker) != len(other._marker):
            return False
        for i in range(len(self._marker)):
            for j in range(len(other._marker)):
                if self._marker[i][j] != other._marker[i][j]:
                    return False
        return True

    def __str__(self)->str:
        s = ""
        for k in range(len(self._marker)):
            s += "---"
        s += "\n"
        for i in range(len(self._marker)):
            for j in range(len(self._marker)):
                s += ' '
                if self._marker[i][j] == "#":
                    s += " "
                else:
                    s += self._marker[i][j]
                s += " "
            s += "\n"
        return s


    # TODO (Task 3)
    # override extensions
    # legal extensions consist of all configurations that can be reached by
    # making a single jump from this configuration

    def extensions(self)-> List[GridPegSolitairePuzzle]:
        xx2 = [0,0,2,-2] #used xx1 and yy1 to move 1 unit on x and y axis.
        yy2 = [2,-2,0,0] #used xx2 and yy2 to move 2 units on x and y axis.
        xx1 = [0,0,1,-1]
        yy1 = [1,-1,0,0]
        ext_list=[]
        for i in range(len(self._marker)):
            for j in range(len(self._marker)):
                if self._marker[i][j] == ".":
                    for k in range(4):
                        if (i+yy2[k] >= 0 and i+yy2[k] < len(self._marker)) and (j+xx2[k] >= 0 and j+xx2[k] < len(self._marker)):
                            if self._marker[i+yy2[k]][j+xx2[k]] == "*":
                                if self._marker[i+yy1[k]][j+xx1[k]] == "*":
                                    new_grid = self.copy_grid_helper()
                                    new_grid._marker[i][j] = "*"
                                    new_grid._marker[i+yy2[k]][j+xx2[k]] = "."
                                    new_grid._marker[i+yy1[k]][j+xx1[k]] = "."
                                    ext_list.append(new_grid)
        return ext_list


    #helper
    def copy_grid_helper(self):
        """Creates a copy of a nested list.i.e.grid"""
        lg = []
        for l in range(len(self._marker)):
            rowlist = []
            for m in range(len(self._marker)):
                rowlist.append(self._marker[l][m])
            lg.append(rowlist)
        new_g = GridPegSolitairePuzzle(lg, self._marker_set)
        return new_g







    # TODO (Task 3)
    # override is_solved
    # A configuration is solved when there is exactly one "*" left

    def is_solved(self) -> bool:
        counter = 0
        for i in range(len(self._marker)):
            for j in range(len(self._marker)):
                if self._marker[i][j] == "*":
                    counter += 1

        if counter > 1:
            return False
        else:
            return True


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    from puzzle_tools import depth_first_solve

    grid = [["*", "*", "*", "*", "*"],
            ["*", "*", "*", "*", "*"],
            ["*", "*", "*", "*", "*"],
            ["*", "*", ".", "*", "*"],
            ["*", "*", "*", "*", "*"]]
    gpsp = GridPegSolitairePuzzle(grid, {"*", ".", "#"})
    print(gpsp)
    # import time
    #
    # start = time.time()
    # solution = depth_first_solve(gpsp)
    # end = time.time()
    # print("Solved 5x5 peg solitaire in {} seconds.".format(end - start))
    # print("Using depth-first: \n{}".format(solution))



