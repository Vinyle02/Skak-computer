import graphics
from boardstate import *


if __name__ == '__main__':
    keep_playing = True

    #random_start = random.randint(0, 1)
    random_start = 1
    board = Board(game_mode=random_start, ai=True, depth=1, log=True)  # game_mode == 0: whites down / 1: blacks down

    while keep_playing:
        graphics.initialize()
        board.place_pieces()
        graphics.draw_background(board)
        keep_playing = graphics.start(board)
        