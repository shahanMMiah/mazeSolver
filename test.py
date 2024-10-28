import unittest

from maze import Maze
from window import Window


class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        window = Window(600, 500, "cells test")
        num_cols = 12
        num_rows = 10
        m1 = Maze(1, 1, num_rows, num_cols, 50, 50, window)
        self.assertEqual(
            len(m1._cells),
            num_cols,
    ) 

        self.assertEqual(
            len(m1._cells[0]),
            num_rows,
        )  

if __name__ == "__main__":
    unittest.main()