Conway's Game of Life
Implemented in Python

Input args to gol.py:
1. A filename

Each character in the input file (given by argument 1) is parsed as a cell in the game world. '1' is parsed as a living cell, newline characters are parsed as new lines in the world (which is created from the top-left corner), every other character is parsed as a dead cell.

The input world is assumed to be rectangular. In particular, all lines of the input file should be of equal length. Otherwise, gol.py will return an error.
