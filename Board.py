class Board:
    def __init__(self, height, width, state=None):
        self.height = height
        self.width = width

        if state:
            # quick check if state dim. OK
            if len(state) == height:
                if len(state[0]) == width:
                    self.state = state
                else:
                    state = None
            else:
                state = None
        
        if not state:
            self.state = []
            [self.state.append(['.']*width) for _ in range(height)]


    def addChipOnColumn(self, col_n, isPlayer1):
        if col_n not in self.validMove():
            return False
        for i in range(self.height):
            if self.state[i][col_n] == '.':
                self.state[i][col_n] = 'O' if isPlayer1 else 'X'
                break
        return True

    def validMove(self):
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

    # returns 1 if player 1 wins, 2 if player 2 wins, 0 if draw, -1 if game still ongoing
    def evaluate(self):
        # Check for draw
        countEmpty = 0
        for row in self.state:
            countEmpty += row.count('.')
        if countEmpty == 0:
            return 0

        # Check for 4 in rows
        for row in self.state:
            counterX = 0
            counterO = 0
            for s in row:
                if s == 'X':
                    counterX += 1
                    counterO = 0
                elif s == 'O':
                    counterX = 0
                    counterO += 1
                else:
                    counterX = 0
                    counterO = 0

                if counterO == 4:
                    return 1
                elif counterX == 4:
                    return 2
            
        # Check for 4 in columns
        stateTransposed = []
        for i in range(self.width):
            row = []
            for j in range(self.height):
                row.append(self.state[j][i])
            stateTransposed.append(row)

        for row in stateTransposed:
            counterX = 0
            counterO = 0
            for s in row:
                if s == 'X':
                    counterX += 1
                    counterO = 0
                elif s == 'O':
                    counterX = 0
                    counterO += 1
                else:
                    counterX = 0
                    counterO = 0

                if counterO == 4:
                    return 1
                elif counterX == 4:
                    return 2

        # Check for 4 in positive diagonal 
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

        for row in stateDiagPos:
            counterX = 0
            counterO = 0
            for s in row:
                if s == 'X':
                    counterX += 1
                    counterO = 0
                elif s == 'O':
                    counterX = 0
                    counterO += 1
                else:
                    counterX = 0
                    counterO = 0

                if counterO == 4:
                    return 1
                elif counterX == 4:
                    return 2

        # Check for 4 in negative diagonal 
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

        for row in stateDiagNeg:
            counterX = 0
            counterO = 0
            for s in row:
                if s == 'X':
                    counterX += 1
                    counterO = 0
                elif s == 'O':
                    counterX = 0
                    counterO += 1
                else:
                    counterX = 0
                    counterO = 0

                if counterO == 4:
                    return 1
                elif counterX == 4:
                    return 2

        return -1