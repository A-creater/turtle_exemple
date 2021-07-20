import turtle

class Checker(turtle.Turtle):
    def __init__(self, i, j, size, color):
        super().__init__(shape='circle')
        self.up()
        self.fillcolor(color)
        self.pencolor('green')
        self.goto(i * size - 100, j * size - 100)
        self.shapesize(1.5, 1.5, 1)

class SquareBoard(turtle.Turtle):
    def __init__(self, i, j, size, color):
        super().__init__(shape='square')
        # self.size = size
        self.up()
        self.fillcolor(color)
        self.goto(i * size - 100, j * size - 100)
        self.shapesize(2, 2)


class Board(turtle.Turtle):
    board = []
    size = 800
    count = 8
    checkers = []

    def __init__(self, size, count):
        super().__init__()
        self.size = size
        self.count = count
        self.create_board()
        self.create_checkers()

    def create_board(self):
        for i in range(self.count):
            board_line = []
            for j in range(self.count):
                color = (i + j) % 2
                color = 'black' if color == 1 else 'white'
                board_line.append(SquareBoard(i, j, 40, color=color))

            self.board.append(board_line)

    def main_bioganal(self):
        for i in range(self.count):
            chess_line = []

            for j in range(self.count):
                # if i == self.count - j - 1:
                if j <= self.count - i - 1 and j >= i:
                    checker = Checker(i, j, 40, 'black')
                    chess_line.append(checker)
                    continue
                # if i == j:
                    checker = Checker(i, j, 40, 'white')
                    chess_line.append(checker)
                    continue

                chess_line.append(None)

            self.checkers.append(chess_line)


    def cross(self):
        for i in range(self.count):
            chess_line = []

            for j in range(self.count):
                m_diagonal = i
                s_diagonal = self.count - i - 1
                if j <= s_diagonal and j >= m_diagonal :
                    checker = Checker(i, j, 20, 'black')
                    chess_line.append(checker)
                    continue
                if j >= s_diagonal and j <= m_diagonal :
                    checker = Checker(i, j, 20, 'white')
                    chess_line.append(checker)
                    continue

                chess_line.append(None)

            self.checkers.append(chess_line)

    def diff(self):
        for i in range(self.count):
            chess_line = []

            for j in range(self.count):
                m_diagonal = i
                s_diagonal = self.count - i - 1
                if j < s_diagonal and j > m_diagonal :
                    if i % 2 == 0:
                        color = 'brown'
                    else:
                        color = 'lightblue'
                    checker = Checker(i, j, 20, color)
                    chess_line.append(checker)
                    continue
                if j < s_diagonal and i > j:
                    if j % 2 == 1:
                        color = 'brown'
                    else:
                        color = 'lightblue'
                    checker = Checker(i, j, 20, color)
                    chess_line.append(checker)
                    continue
                if i == j or j == s_diagonal:
                    color = 'lightblue'
                    checker = Checker(i, j, 20, color)
                    chess_line.append(checker)
                    continue

                chess_line.append(None)

            self.checkers.append(chess_line)


    def create_checkers(self):
        self.main_bioganal()
        # for i in range(self.count):
        #     chess_line = []
        #
        #     for j in range(self.count):
        #         is_set = (i + j) % 2
        #
        #         if is_set:
        #             if i < 3:
        #                 c = .2 + i / 8
        #                 checker = Checker(i, j, 40, (c, c, c))
        #                 chess_line.append(checker)
        #                 continue
        #             if i >= 5:
        #                 c = 0 + (i / 8)
        #                 checker = Checker(i, j, 40, (c + 0.1, c + 0.1, c))
        #                 chess_line.append(checker)
        #                 continue
        #
        #         chess_line.append(None)
        #
        #     self.checkers.append(chess_line)

    def move(self, i1, j1, i2, j2):
        f: Checker = self.checkers[i1][j1]
        if f is None:
            return

        f.goto(i2 * 20, j2 * 20)

        self.checkers[i2][j2] = f
        self.checkers[i1][j1] = None




board = Board()

# board.move(2, 3, 3, 2)
# board.move(5, 0, 4, 1)
# board.move(3, 2, 5, 0)







turtle.done()
