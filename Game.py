import random
from Board import Board

class Game:
    def __init__(self, param):

        self.board = Board(param['boardHeight'], param['boardWidth'])
        self.turnCounter = 0
        self.player1Turn = bool(random.randint(0,1))
        self.gameIsOver = False

    def startPlay(self):
        while(not self.gameIsOver):
            currentPlayer = 1 if self.player1Turn else 2
            currentChip = 'O' if self.player1Turn else 'X'
            self.board.display()
            col_n = int(input(f"Player {currentPlayer}'s move ({currentChip}): "))
            while not self.board.addChipOnColumn(col_n, self.player1Turn):
                print("Move not valid")
                col_n = int(input(f"Player {currentPlayer}'s move : "))
            self.player1Turn = not self.player1Turn

            result = self.board.evaluate()
            if result != -1:
                self.gameIsOver = True
                self.board.display()
                if result == 0:
                    print("Game Over - Draw !")
                else:
                    print(f"Game Over - Player {result} won !")
