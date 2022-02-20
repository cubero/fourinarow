from Game import Game

## For debugging:
# from Board import Board

# state = [['.', '.', '.', '.', '.', 'X','O'],
# ['.', '.', '.', '.', '.', 'X','O'],
# ['.', '.', '.', '.', '.', 'X','.'],
# ['.', '.', '.', '.', '.', '.','.'],
# ['.', '.', '.', '.', '.', '.','.'],
# ['.', '.', '.', '.', '.', '.','.']]
# board = Board(6,7, state)

gameParameters = {}
gameParameters['boardWidth'] = 7
gameParameters['boardHeight'] = 6
gameParameters['player2'] = 'computer'

game = Game(gameParameters)
game.startPlay()