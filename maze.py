""" Module for creat points, lines, cells and maze objects. """

from tkinter import Canvas
import random

from window import Window


class Point:
    """Class for 2D positions."""

    def __init__(self, x: float, y: float):
        self._x = x
        self._y = y

    def get_x(self):
        """Get x axis value."""
        return self._x

    def get_y(self):
        """Get y axis value."""
        return self._y


class Line:
    """Class for creating drawable lines"""

    def __init__(self, p1: Point, p2: Point, width=2):
        """Initilise position and width.

        Args:
            p1 (Point): Start point
            p2 (Point): End point
            width (int, optional): width of line. Defaults to 2.
        """
        self._p1 = p1
        self._p2 = p2
        self._width = width

    def get_p1(self):
        """Get the start point

        Returns:
            Point: The point object
        """
        return self._p1

    def get_p2(self):
        """Get the end point

        Returns:
            Point: The point object
        """
        return self._p2

    def draw(self, canvas: Canvas, color="black"):
        """Draw the line to the canvas

        Args:
            canvas (Canvas): Window class canvas object
            color (str, optional): color for drawn line. Defaults to "black".
        """
        canvas.create_line(
            self._p1.get_x(),
            self._p1.get_y(),
            self._p2.get_x(),
            self._p2.get_y(),
            fill=color,
            width=self._width,
        )


class Cell:
    """Class for maze cell"""

    def __init__(
        self,
        point: Point,
        win: Window,
        size_x=20.0,
        size_y=20.0,
        line_wdith=2,
    ):
        """Initialise the cell position, size, visited and walls attribs

        Args:
            point (Point): position of cell
            win (Window): window to draw to
            size_x (float, optional): size of cell width. Defaults to 20.0.
            size_y (float, optional): size of cell height. Defaults to 20.0.
            line_wdith (int, optional): size of line width. Defaults to 2.
            visited (bool, optional): cell visited. Defaults to False.
        """

        self.left_wall = True
        self.right_wall = True
        self.top_wall = True
        self.bot_wall = True

        self._pos = point
        self._win = win
        self._size_x = size_x
        self._size_y = size_y
        self._line_width = line_wdith
        self.visited = False

    def get_mid(self):
        """Get mid point of cell

        Returns:
            Point: midpoint point object
        """

        return Point(
            (self._pos.get_x() + self._pos.get_x() + self._size_x) / 2,
            (self._pos.get_y() + self._pos.get_y() + self._size_y) / 2,
        )

    def draw(self):
        """Draw the cell to window"""

        x = self._pos.get_x()
        y = self._pos.get_y()

        top_line = Line(self._pos, Point(x + self._size_x, y), self._line_width)
        bot_line = Line(
            Point(x, y + self._size_y),
            Point(x + self._size_x, y + self._size_y),
            self._line_width,
        )
        left_line = Line(self._pos, Point(x, y + self._size_y), self._line_width)
        right_line = Line(
            Point(x + self._size_x, y),
            Point(x + self._size_x, y + self._size_y),
            self._line_width,
        )

        walls = [self.top_wall, self.bot_wall, self.left_wall, self.right_wall]
        col = "black"
        for num, line in enumerate([top_line, bot_line, left_line, right_line]):

            if walls[num]:
                col = "black"
            else:
                col = "#d9d9d9"

            line.draw(self._win.get_canvas(), col)

    def draw_move(self, to_cell, undo=False):
        """Draw a line connecting current cell to another

        Args:
            to_cell (Cell): The other cell object
            undo (bool, optional): draw and undo line. Defaults to False.
        """

        cell_frm = self
        cell_to = to_cell
        col = "red"

        if undo:
            cell_frm = self
            cell_to = to_cell
            col = "grey"

        connect_line = Line(cell_frm.get_mid(), cell_to.get_mid(), self._line_width)
        connect_line.draw(self._win.get_canvas(), col)


class Maze:
    """Class to create and solve the maze"""

    def __init__(
        self,
        x1: int,
        y1: int,
        num_rows: int,
        num_cols: int,
        cell_size_x: int,
        cell_size_y: int,
        win: Window,
        animation_speed=20,
        seed=None,
    ):
        """Initialise size, row and column count,  populate with cells and create maze path

        Args:
            x1 (int): x pos of maze
            y1 (int): y pos of maze
            num_rows (int): number of rows
            num_cols (int): number of colums
            celll_size_x (int): cells width
            cell_size_y (int): cells height
            win (Window): window to draw to
            animation_speed (int, optional): speed of draw rate Defaults to 20.
            seed (_type_, optional): seed for randomizer. Defaults to None.
        """
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win
        self._aniamtion_speed = animation_speed
        self._seed = seed

        self._cells = []
        self._create_cells()
        self._break_entrance_and_exit()
        self._break_walls_r(0, 0)
        self._reset_visited()

    def _create_cells(self):
        """Populate cells list with cell objects"""
        x_pos = self._x1

        for col_num in range(self._num_cols):
            y_pos = self._y1
            self._cells.append([])
            orig_y_pos = y_pos
            for row_num in range(self._num_rows):

                cell = Cell(
                    Point(x_pos, y_pos),
                    self._win,
                    self._cell_size_x,
                    self._cell_size_y,
                )

                self._cells[col_num].append(cell)
                cell.draw()
                self._animate()

                y_pos = self._cell_size_y * (row_num + 1) + orig_y_pos
            x_pos += self._cell_size_x

    def get_cells(self):
        """Return list of cells

        Returns:
            list: cells list
        """
        return self._cells

    def _animate(self):
        """Redraw with a wait offset"""
        self._win.redraw()
        self._win.get_canvas().after(self._aniamtion_speed)

    def _break_entrance_and_exit(self):
        """Break the outside walls to entrance and exit"""

        self._cells[0][0].left_wall = False
        self._cells[0][0].draw()
        self._cells[-1][-1].right_wall = False
        self._cells[-1][-1].draw()

    def _get_cell_dirs(self, i: int, j: int):
        """Get the available directions of current cell as a dict

        Args:
            i (int): cell row number
            j (int): cell column number

        Returns:
            dict: direction name and row/col delta values
        """
        to_visit = {}
        direction_map = {
            "bot": (i, j + 1),
            "top": (i, j - 1),
            "left": (i - 1, j),
            "right": (i + 1, j),
        }
        for cell_dir, dir_vals in direction_map.items():
            if (
                dir_vals[0] >= 0
                and dir_vals[0] < self._num_cols
                and dir_vals[1] >= 0
                and dir_vals[1] < self._num_rows
            ):

                to_visit[cell_dir] = direction_map[cell_dir]

        return to_visit

    def _break_walls_r(self, i: int, j: int):
        """Break walls to make path to end cell

        Args:
            i (int): current cell pos row
            j (int): current cell pos collumn
        """

        to_visit = self._get_cell_dirs(i, j)

        current_node = self._cells[i][j]
        current_node.visited = True
        while True:

            if not to_visit:
                current_node.draw()
                self._animate()
                return

            random.seed(self._seed)
            keys = list(to_visit.keys())

            rand_key = keys[random.randint(0, len(keys) - 1)]

            move_to = to_visit.pop(rand_key, None)

            move_node = self._cells[move_to[0]][move_to[1]]

            if not move_node.visited:
                match rand_key:
                    case "top":
                        current_node.top_wall = False
                        move_node.bot_wall = False
                    case "bot":
                        current_node.bot_wall = False
                        move_node.top_wall = False
                    case "left":
                        current_node.left_wall = False
                        move_node.right_wall = False
                    case "right":
                        current_node.right_wall = False
                        move_node.left_wall = False

                self._break_walls_r(move_to[0], move_to[1])

    def _reset_visited(self):
        """Reset all cell visited status"""
        for col_num in range(self._num_cols):
            for row_num in range(self._num_rows):
                self._cells[col_num][row_num].visited = False

    def solve(self):
        """Main solve call method

        Returns:
            bool: if maze was solved
        """
        return self.solve_r(0, 0)

    def solve_r(self, i: int, j: int):
        """recursivly move to next available cell to the end

        Args:
            i (int): current cell pos row
            j (int): current cell pos collumn

        Returns:
            bool: if the right path was found
        """

        self._animate()

        current_cell = self._cells[i][j]
        current_cell.visited = True

        if current_cell == self._cells[-1][-1]:
            return True
        cell_dirs = self._get_cell_dirs(i, j)

        for cell_dir, dir_val in cell_dirs.items():

            to_cell = self._cells[dir_val[0]][dir_val[1]]
            blocked = False

            match cell_dir:
                case "top":
                    blocked = current_cell.top_wall

                case "bot":
                    blocked = current_cell.bot_wall

                case "left":
                    blocked = current_cell.left_wall

                case "right":
                    blocked = current_cell.right_wall

            if to_cell.visited:
                blocked = True

            if not blocked:

                current_cell.draw_move(to_cell)

                right_path = self.solve_r(dir_val[0], dir_val[1])

                if right_path:
                    return True

                current_cell.draw_move(to_cell, undo=True)

        return False
