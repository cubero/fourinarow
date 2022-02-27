class Board:
    def __init__(self, height, width):
        self.height = height
        self.width = width
        self.state = []
        [self.state.append(['.']*width) for _ in range(height)]


    def addChipOnColumn(self, col_n, isPlayer1):
        if col_n not in self.validMoves():
            return False
        for i in range(self.height):
            if self.state[i][col_n] == '.':
                self.state[i][col_n] = 'O' if isPlayer1 else 'X'
                break
        return True

    def validMoves(self):
        validMoveList = []
        for i in range(self.width):
            if self.state[self.height-1][i] == '.':
                validMoveList.append(i)
        return validMoveList

    def display(self):
        for i in range(self.width):
            space = 2 if i < 10 else 1
            print("  " + str(i) + " "*space, end='')
        print('')
        print("_"*self.width*5)
        for i in range(self.height-1,-1,-1):
            for j in range(self.width):
                print("  " + self.state[i][j] + "  ", end='')
            print("\n",  end='\r')
        print("-"*self.width*5)

    # return 0 if game if over in draw
    # else return the amount of chips in a row
    # if < 4, there must still be place around to make 4 to count
    def evaluate(self, chip): 
        # Check for draw
        if len(self.validMoves()) == 0:
            return 0

        stateTransposed = []
        for i in range(self.width):
            row = []
            for j in range(self.height):
                row.append(self.state[j][i])
            stateTransposed.append(row)

        stateDiagPos = []
        for i in range(self.width):
            h = i; v = 0
            diag = []
            while h < self.width and v < self.height:
                diag.append(self.state[v][h])
                h += 1; v += 1
            stateDiagPos.append(diag)
        for j in range(1, self.height):
            h = 0; v = j
            diag = []
            while h < self.width and v < self.height:
                diag.append(self.state[v][h])
                h += 1; v += 1
            stateDiagPos.append(diag)

        stateDiagNeg = []
        for i in range(self.width):
            h = i; v = 0
            diag = []
            while h >= 0 and v < self.height:
                diag.append(self.state[v][h])
                h -= 1; v += 1
            stateDiagNeg.append(diag)
        for j in range(1, self.height):
            h = self.width - 1 ; v = j
            diag = []
            while h >= 0 and v < self.height:
                diag.append(self.state[v][h])
                h -= 1; v += 1
            stateDiagNeg.append(diag)

        maxScore = 0
        for row in (self.state + stateTransposed + stateDiagPos + stateDiagNeg):
            s = ''.join(row)

            if chip*4 in s:
                return 20
            elif ('.'+chip*3) in s or (chip*3+'.') in s or (chip+'.'+2*chip) in s or (2*chip+'.'+chip) in s:
                maxScore = 3
            elif ('..'+chip*2) in s or (chip*2+'..') in s or ('.'+chip*2+'.') in s or (chip+'..'+chip) in s:
                maxScore = max(maxScore, 2)
            else:
                maxScore = max(maxScore, 1)

        return maxScore

    # for the minimax algorithm
    def undoMove(self, move):
        for i in range(self.height-1, -1, -1):
            if self.state[i][move] == 'X' or self.state[i][move] == 'O':
                self.state[i][move] = '.'
                return True
        return False