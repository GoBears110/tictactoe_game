class Board:

    def __init__(self, n):
        self.cells = [[' ' for i in range(n)] for j in range(n)]
        self.size = n

    def changePiece(self, row, col, playerPiece):
        self.cells[row][col] = playerPiece

    def display(self):
        self.board = ''
        for i in range(self.size):
            for j in range(self.size):
                if j > 0:
                    self.board += '|'
                self.board += ' ' + str(self.cells[i][j]) + ' '
            if i < self.size-1:
                self.board += '\n' + ('----' * self.size)
            self.board += '\n'
        print(self.board)


