import random
from Board import Board

class Game:
    def __init__(self, param):

        self.board = Board(param['boardHeight'], param['boardWidth'])
        self.player2IsHuman = False if param['player2'] == 'computer' else True
        self.turnCounter = 0
        self.player1Turn = bool(random.randint(0,1))
        self.gameIsOver = False

    def startPlay(self):
        while(not self.gameIsOver):
            self.board.display()
            self.getPlayersMove()

            player1Status = self.board.evaluate('O')
            player2Status = self.board.evaluate('X')
            if player1Status == 4 or player2Status == 4:
                self.gameIsOver = True
                self.board.display()
                print(f"Game Over - Player {1 if player1Status==4 else 2} won !")
            elif player1Status == 0:
                self.gameIsOver = True
                self.board.display()
                print("Game Over - Draw !")
            else:
                self.player1Turn = not self.player1Turn

    def getPlayersMove(self):
        currentPlayer = 1 if self.player1Turn else 2
        currentChip = 'O' if self.player1Turn else 'X'

        if self.player1Turn or self.player2IsHuman:
            col_n = int(input(f"Player {currentPlayer}'s move ({currentChip}): "))
            while not self.board.addChipOnColumn(col_n, self.player1Turn):
                print("Move not valid")
                col_n = int(input(f"Player {currentPlayer}'s move : "))

        else:   # Playing against the AI
            validMove = False
            while not validMove:
                validMove = self.board.addChipOnColumn(random.randint(0,self.board.width), self.player1Turn)

            # for debugging:
            print(f"Player 1's status = {self.board.evaluate('O')}")
            print(f"Player 2's status = {self.board.evaluate('X')}")