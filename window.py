""" Module for creating Window class object """
from tkinter import Tk, Canvas

class Window:
    """tkinter window and canvas class 
    """
    def __init__(self, width: float, height: float, title):
        """ init canvas and window 

        Args:
            width (float): width of window
            height (float): height of window
            title (str): window top title 
        """
        self._root = Tk()
        self._root.title(title)

        self._root.minsize(width, height)
        self._canvas = Canvas(self._root)
        self._canvas.config(width=width, height=height)
        self._canvas.pack()

        self._running = False
        self._root.protocol("WM_DELETE_WINDOW", self._close)

    def get_canvas(self):
        """ Get canvas object

        Returns:
            Canvas: The Canvas object
        """
        return self._canvas

    def redraw(self):
        """ Update Maze and redraw the canvas  
        """
        self._root.update_idletasks()
        self._root.update()

    def wait_for_close(self):
        """ Main loop for running window 
        """
        self._running = True
        while self._running:
            self.redraw()

    def _close(self):
        """ Close the window 
        """
        self._running = False

    def draw_line(self, line, color="black"):
        """ Draw a line object to the canvas

        Args:
            line (Line): line object
            color (str, optional): color of line. Defaults to "black".
        """

        line.draw(self._canvas, color)
