import unittest

from maze import Maze
from window import Window


class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        window = Window(600, 500, "create cells test")
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
    def test_maze_resets_visited(self):
        window = Window(600, 500, "reset visited test")
        num_cols = 12
        num_rows = 10
        m1 = Maze(1, 1, num_rows, num_cols, 50, 50, window)
        
        is_reset = True
        for c in range(num_cols):
            for r in range(num_rows):
                if m1._cells[c][r].visited:
                    is_reset = False
        
        self.assertTrue(is_reset)

    def test_maze_reaches_end(self):
        window = Window(600, 500, "reaches end test")
        num_cols = 12
        num_rows = 10
        m1 = Maze(1, 1, num_rows, num_cols, 50, 50, window)
        
        is_wall_broken = False
        end_cell = m1._cells[-1][-1]
        for wall in [end_cell.left_wall,end_cell.right_wall,end_cell.top_wall,end_cell.bot_wall]:
            if not wall:
                is_wall_broken = True
        
        
        self.assertTrue(is_wall_broken)

    def test_maze_solved(self):
        window = Window(600, 500, "maze solved test")
        num_cols = 12
        num_rows = 10
        m1 = Maze(1, 1, num_rows, num_cols, 50, 50, window)

        self.assertTrue(m1.solve())
        
        

if __name__ == "__main__":
    unittest.main()