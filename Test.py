from Board import Board

board = Board(6,7)

board.addChipOnColumn(3, True)
board.display()
board.undoMove(3)
board.display()