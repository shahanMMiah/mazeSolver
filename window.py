from tkinter import Tk, BOTH, Canvas

class Window:
    def __init__(self, width: float, height: float, title):

        self._root = Tk()
        self._root.title(title)

        self._root.minsize(width, height)
        self._canvas = Canvas(self._root)
        self._canvas.config(width=width, height=height)
        self._canvas.pack()

        self._running = False
        self._root.protocol("WM_DELETE_WINDOW", self._close)

    def get_canvas(self):
        return self._canvas

    def redraw(self):
        self._root.update_idletasks()
        self._root.update()

    def wait_for_close(self):
        self._running = True
        while self._running:
            self.redraw()

    def _close(self):
        self._running = False

    def draw_line(self, line, color="black"):

        line.draw(self._canvas, color)


