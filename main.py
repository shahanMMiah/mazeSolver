from maze import Maze
from window import Window


def main():
    width = 500
    height = 500
    window = Window(width, height, "Maze Solver")

    square_amount = 15

    cols = width / square_amount 
    rows = height / square_amount

    maze = Maze(1, 1, square_amount, square_amount, cols, rows, window)
    maze.solve()

    window.wait_for_close()



if __name__ == "__main__":
    main()
