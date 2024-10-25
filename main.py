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
        win: Window,
        size = 20.0
        ):

        self.left_wall = left
        self.right_wall = right
        self.top_wall = top
        self.bot_wall = bot

        self.pos = point
        self.win = win
        self.size = size
    def get_mid(self):
        
        return(Point((self.pos.x +self.pos.x + self.size)/2, (self.pos.y + self.pos.y+self.size)/2))

    def draw(self):
        
        x = self.pos.x
        y = self.pos.y

        top_line = Line(self.pos, Point(x + self.size, y))
        bot_line = Line(Point(x , y+self.size), Point(x + self.size, y+ self.size))
        left_line = Line(self.pos, Point(x , y + self.size))
        right_line = Line(Point(x+self.size , y), Point(x +self.size, y+self.size))
        
        if self.top_wall:
            top_line.draw(self.win.canvas)
        if self.bot_wall:
            bot_line.draw(self.win.canvas)
        if self.left_wall:
            left_line.draw(self.win.canvas)
        if self.right_wall:
            right_line.draw(self.win.canvas)


    def draw_move(self, to_cell, undo=False):
        
        cell_frm = self
        cell_to = to_cell
        col = "red"
        
        if undo:
            cell_frm = self
            cell_to = to_cell
            col = "gray"

        connect_line = Line(cell_frm.get_mid(), cell_to.get_mid())
        connect_line.draw(self.win.canvas, col)        
            
        

def main():
    window = Window(500,500,"test")

    line1 = Line(Point(100,0),Point(100, 100))
    #window.draw_line(line1)

    test_cell = Cell(True,True,True,True,Point(100,300),window)
    test_cell2 = Cell(True,True,True,True,Point(200,300),window)

    test_cell.draw()
    test_cell2.draw()
    
    test_cell.draw_move(test_cell2 )
    
    window.wait_for_close()
    print("hello")

main()