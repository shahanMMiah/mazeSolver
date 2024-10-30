from maze import Maze
from window import Window


def main():
    width = 500
    height = 500
    window = Window(width, height, "test")

    square_amount = 15

    cols = width / square_amount 
    rows = height / square_amount

    maze = Maze(1, 1, square_amount, square_amount, cols, rows, window)

    """
    line1 = Line(Point(100, 0), Point(100, 100))
    # window.draw_line(line1)

    test_cell = Cell(True, True, True, True, Point(100, 300), window,50, 30, 5)
    test_cell2 = Cell(True, True, True, True, Point(200, 300), window, 20, 40)

    test_cell.draw()
    test_cell2.draw()

    test_cell.draw_move(test_cell2)
    """

    window.wait_for_close()
    print("hello")


if __name__ == "__main__":
    main()
