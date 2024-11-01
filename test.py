"""maze solver test module. """

import unittest
from maze import Maze
from window import Window


class Tests(unittest.TestCase):
    """Test class for maze solver aspacts

    Args:
        unittest (TestCase): deriving from unittest TestCase class
    """

    def test_maze_create_cells(self):
        """Test if cells are create"""
        window = Window(600, 500, "create cells test")
        num_cols = 12
        num_rows = 10
        m1 = Maze(1, 1, num_rows, num_cols, 50, 50, window)
        self.assertEqual(
            len(m1.get_cells()),
            num_cols,
        )

        self.assertEqual(
            len(m1.get_cells()[0]),
            num_rows,
        )

    def test_maze_resets_visited(self):
        """Test if resets cell visited attribute"""
        window = Window(600, 500, "reset visited test")
        num_cols = 12
        num_rows = 10
        m1 = Maze(1, 1, num_rows, num_cols, 50, 50, window)

        is_reset = True
        for c in range(num_cols):
            for r in range(num_rows):
                if m1.get_cells()[c][r].visited:
                    is_reset = False

        self.assertTrue(is_reset)

    def test_maze_reaches_end(self):
        """Test if maze can reach end cell"""
        window = Window(600, 500, "reaches end test")
        num_cols = 12
        num_rows = 10
        m1 = Maze(1, 1, num_rows, num_cols, 50, 50, window)

        is_wall_broken = False
        end_cell = m1.get_cells()[-1][-1]
        for wall in [
            end_cell.left_wall,
            end_cell.right_wall,
            end_cell.top_wall,
            end_cell.bot_wall,
        ]:
            if not wall:
                is_wall_broken = True

        self.assertTrue(is_wall_broken)

    def test_maze_solved(self):
        """Test if solve method returns true"""
        window = Window(600, 500, "maze solved test")
        num_cols = 12
        num_rows = 10
        m1 = Maze(1, 1, num_rows, num_cols, 50, 50, window)

        self.assertTrue(m1.solve())


if __name__ == "__main__":
    unittest.main()
