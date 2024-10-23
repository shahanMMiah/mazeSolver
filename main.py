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
        self.canvas = Canvas(self.root) 
        self.canvas.width = width
        self.canvas.height = height
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


def main():
    window = Window(200,200,"test")

    line1 = Line(Point(100,0),Point(100, 100))
    window.draw_line(line1)
    window.wait_for_close()
    print("hello")

main()