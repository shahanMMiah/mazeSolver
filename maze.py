from window import Window
from tkinter import Canvas

class Point:
    def __init__(self, x: float, y: float):
        self._x = x
        self._y = y

    def get_x(self):
        return self._x

    def get_y(self):
        return self._y


class Line:
    def __init__(self, p1: Point, p2: Point, width=2):
        self._p1 = p1
        self._p2 = p2
        self._width = width

    def get_p1(self):
        return self._p1

    def get_p2(self):
        return self._p2

    def draw(self, canvas: Canvas, color="black"):
        canvas.create_line(
            self._p1.get_x(),
            self._p1.get_y(),
            self._p2.get_x(),
            self._p2.get_y(),
            fill=color,
            width=self._width,
        )


class Cell:
    def __init__(
        self,
        left: bool,
        right: bool,
        top: bool,
        bot: bool,
        point: Point,
        win: Window,
        size_x=20.0,
        size_y=20.0,
        line_wdith=2,
    ):

        self.left_wall = left
        self.right_wall = right
        self.top_wall = top
        self.bot_wall = bot

        self._pos = point
        self._win = win
        self._size_x = size_x
        self._size_y = size_y
        self._line_width = line_wdith

    def get_mid(self):

        return Point(
            (self._pos.get_x() + self._pos.get_x() + self._size_x) / 2,
            (self._pos.get_y() + self._pos.get_y() + self._size_y) / 2,
        )

    def draw(self):

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

        if self.top_wall:
            top_line.draw(self._win.get_canvas())
        if self.bot_wall:
            bot_line.draw(self._win.get_canvas())
        if self.left_wall:
            left_line.draw(self._win.get_canvas())
        if self.right_wall:
            right_line.draw(self._win.get_canvas())

    def draw_move(self, to_cell, undo=False):

        cell_frm = self
        cell_to = to_cell
        col = "red"

        if undo:
            cell_frm = self
            cell_to = to_cell
            col = "gray"

        connect_line = Line(cell_frm.get_mid(), cell_to.get_mid(), self._line_width)
        connect_line.draw(self._win.get_canvas(), col)


class Maze:
    def __init__(
        self,
        x1: int,
        y1: int,
        num_rows: int,
        num_cols: int,
        celll_size_x: int,
        cell_size_y: int,
        win: Window,
        animation_speed = 70
    ):
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = celll_size_x
        self._cell_size_y = cell_size_y
        self._win = win
        self._aniamtion_speed = animation_speed

        self._cells = []
        self._create_cells()

    def _create_cells(self):
        x_pos = self._x1

        for col_num in range(self._num_cols):
            y_pos = self._y1
            self._cells.append([])
            # x_pos += self._celll_size_x

            for row_num in range(self._num_rows):
                cell = Cell(
                    True,
                    True,
                    True,
                    True,
                    Point(x_pos, y_pos),
                    self._win,
                    self._cell_size_x,
                    self._cell_size_y,
                )

                self._cells[col_num].append(cell)
                cell.draw()
                self._animate()

                y_pos += self._cell_size_y
            x_pos += self._cell_size_x

    def _animate(self):
        self._win.redraw()
        self._win.get_canvas().after(self._aniamtion_speed)
