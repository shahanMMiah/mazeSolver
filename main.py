from tkinter import Tk, BOTH, Canvas

class Point():
    def __init__(self, x : float, y: float):
        self.x = x
        self.y = y

class Line():
    def __init__(self, p1: Point, p2 :Point):
        self.p1 = p1
        self.p2 = p2
    
    def draw(self, canvas: Canvas, color = "black"):
        canvas.create_line(self.p1.x, self.p1.y, self.p2.x, self.p2.y, fill=color, width=2)

        
class Window():
    def __init__(self, width: float, height: float, title):
        
        self.root = Tk()
        self.title = title
    
        self.root.minsize(height, width)       
        self.canvas = Canvas(self.root)
        self.canvas.config(width=width, height=height)
        self.canvas.pack()

        self.running = False
        self.root.protocol("WM_DELETE_WINDOW", self.close)

    def redraw(self):
        self.root.update_idletasks()
        self.root.update()
    def wait_for_close(self):
        self.running = True
        while(self.running):
            self.redraw()
    def close(self):
        self.running = False
    
    def draw_line(self, line: Line, color="black"):
        
        line.draw(self.canvas, color)

class Cell():
    def __init__(
        self, 
        left: bool, 
        right: bool, 
        top: bool,
        bot: bool, 
        point: Point, 
        win: Window
        ):

        self.left_wall = left
        self.right_wall = right
        self.top_wall = top
        self.bot_wall = bot

        self.pos = point
        self.win = win

    def draw(self, size = 20):
        
        
        x = self.pos.x
        y = self.pos.y

        top_line = Line(self.pos, Point(x + size, y))
        bot_line = Line(Point(x , y+size), Point(x + size, y+size))
        left_line = Line(self.pos, Point(x , y + size))
        right_line = Line(Point(x+size , y), Point(x + size, y+size))
        
        if self.top_wall:
            top_line.draw(self.win.canvas)
        if self.bot_wall:
            bot_line.draw(self.win.canvas)
        if self.left_wall:
            left_line.draw(self.win.canvas)
        if self.right_wall:
            right_line.draw(self.win.canvas)



def main():
    window = Window(500,500,"test")

    line1 = Line(Point(100,0),Point(100, 100))
    #window.draw_line(line1)

    test_cell = Cell(True,True,True,True,Point(100,300),window)

    test_cell.draw(100)
    
    window.wait_for_close()
    print("hello")

main()