class XPlayer:
    mark = 'x'
    def __init__(self, board):
        self.board = board
        self.row = len(self.board)
        self.col = len(self.board[0])
    def is_valid_move(self, *coordinate):
        if (len(coordinate) == 1):
            coordinate = coordinate[0]
        try:
            if self.board[coordinate[0]][coordinate[1]] == '.':
                return 1
        except:
            pass
        return 0
    def play(self, *coordinate):
        if (len(coordinate) == 1):
            coordinate = coordinate[0]
        if (self.is_valid_move(coordinate[0], coordinate[1])):
            self.board[coordinate[0]][coordinate[1]] = self.mark
            return 1
        return 0    
    def is_winning_vertically(self):
        for j in range(self.col):
            for i in range(self.row - 4):
                if self.board[i][j] == self.mark:
                    if self.board[i + 1][j] == self.mark:
                        if self.board[i + 2][j] == self.mark:
                            if self.board[i + 3][j] == self.mark:
                                if self.board[i + 4][j] == self.mark:
                                    return 1
        return 0
    def is_winning_horizontally(self):
        for i in range(self.row):
            for j in range(self.col - 4):
                if self.board[i][j] == self.mark:
                    if self.board[i][j + 1] == self.mark:
                        if self.board[i][j + 2] == self.mark:
                            if self.board[i][j + 3] == self.mark:
                                if self.board[i][j + 4] == self.mark:
                                    return 1
        return 0
    def is_winning_diagonally(self):
        for i in range(self.row - 4):
            for j in range(self.col - 4):
                if self.board[i][j] == self.mark:
                    if self.board[i + 1][j + 1] == self.mark:
                        if self.board[i + 2][j + 2] == self.mark:
                            if self.board[i + 3][j + 3] == self.mark:
                                if self.board[i + 4][j + 4] == self.mark:
                                    return 1
        return 0
    def is_winning(self):
        return self.is_winning_vertically() or self.is_winning_horizontally() or self.is_winning_diagonally()
        

class OPlayer(XPlayer):
    mark = 'o'

        
class Board:
    def __init__(self, row = 10, col = 10):
        self.row = row
        self.col = col
        self.board = [['.' for j in range(self.col)] for i in range(self.row)]
        self.xPlayer = XPlayer(self.board)
        self.oPlayer = OPlayer(self.board)
        self.log = []
##    def __getitem__(self, row):
##        return self.board[row]
    def __str__(self):
        return '\n'.join([' '.join([str(cell) for cell in row]) for row in self.board])
    def __repr__(self):
        return '\n'.join([' '.join([str(cell) for cell in row]) for row in self.board])

    
##board = Board()
##print(board)
##print()
##board.xPlayer.play((3, 4))
##print(board)
