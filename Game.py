import random, copy
from Board import Board

minimaxDepth = 5

class Game:
    def __init__(self, param):

        self.board = Board(param['boardHeight'], param['boardWidth'])
        self.player2IsHuman = False if param['player2'] == 'computer' else True
        self.turnCounter = 0
        self.player1Turn = bool(random.randint(0,1))
        self.isOver = False

    def startPlay(self):
        while(not self.isOver):
            self.board.display()
            self.getPlayersMove()

            player1Status = self.board.evaluate('O')
            player2Status = self.board.evaluate('X')
            if player1Status == 20 or player2Status == 20:
                self.isOver = True
                self.board.display()
                print(f"Game Over - Player {1 if player1Status==4 else 2} won !")
            elif player1Status == 0:
                self.isOver = True
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
            simBoard = copy.deepcopy(self.board)
            pos = minimax(simBoard, minimaxDepth, self.player1Turn)
            self.board.addChipOnColumn(pos, self.player1Turn)

            # for debugging:
            # print(f"Player 1's status = {self.board.evaluate('O')}")
            # print(f"Player 2's status = {self.board.evaluate('X')}")

def minimax(board, depth, player1Turn):

    evaluationX = board.evaluate('X')
    evaluationO = board.evaluate('O')
    if evaluationX == 20 or evaluationO == 20 or depth == 0:
        evaluation = evaluationO - evaluationX
        return evaluation

    scores = []
    for move in board.validMoves():
        board.addChipOnColumn(move, player1Turn)
        score = minimax(board, depth - 1, not player1Turn)
        board.undoMove(move)
        scores.append(score)


    if player1Turn:
            return max(scores)
    else:
        if depth == minimaxDepth:
            # print(scores)
            return board.validMoves()[scores.index(min(scores))]
        else:
            return min(scores)