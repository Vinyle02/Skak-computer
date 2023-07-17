from ChessPiece import *
from copy import deepcopy
from TranspositionTables import Heuristics

white_king_has_moved = [False]
black_king_gm1_has_moved = [False]
white_rook_gm0_right_has_moved = [False]
white_rook_gm0_left_has_moved = [False]
black_rook_gm1_right_has_moved = [False]
black_rook_gm1_left_has_moved = [False]

class Board:

    whites = []
    blacks = []
    def __init__(self, game_mode, ai=False, depth=2, log=False):    # game_mode == 0 : whites down/blacks up
        self.board = []
        self.game_mode = game_mode
        self.depth = depth
        self.ai = ai
        self.log = log

    def initialize_board(self):
        for i in range(8):
            self.board.append(['empty-block' for _ in range(8)])

    def place_pieces(self):
        self.board.clear()
        self.whites.clear()
        self.blacks.clear()
        self.initialize_board()
        if self.game_mode == 0:
            self.whiteKing = King('white', 0, 4, '\u265A')
            self.blackKing = King('black', 7, 4, '\u2654')
        else:
            self.whiteKing = King('white', 0, 3, '\u265A')
            self.blackKing = King('black', 7, 3, '\u2654')
        for j in range(8):
            self[1][j] = Pawn('white', 1, j, '\u265F')
            self[6][j] = Pawn('black', 6, j, '\u2659')
        self[0][0] = Rook('white', 0, 0, '\u265C')
        self[0][7] = Rook('white', 0, 7, '\u265C')
        self[0][1] = Knight('white', 0, 1, '\u265E')
        self[0][6] = Knight('white', 0, 6, '\u265E')
        self[0][2] = Bishop('white', 0, 2, '\u265D')
        self[0][5] = Bishop('white', 0, 5, '\u265D')
        if self.game_mode == 0:
            self[0][3] = Queen('white', 0, 3, '\u265B')
            self[0][4] = self.whiteKing
        else:
            self[0][4] = Queen('white', 0, 4, '\u265B')
            self[0][3] = self.whiteKing
        self[7][0] = Rook('black', 7, 0, '\u2656')
        self[7][7] = Rook('black', 7, 7, '\u2656')
        self[7][1] = Knight('black', 7, 1, '\u2658')
        self[7][6] = Knight('black', 7, 6, '\u2658')
        self[7][2] = Bishop('black', 7, 2, '\u2657')
        self[7][5] = Bishop('black', 7, 5, '\u2657')
        if self.game_mode == 0:
            self[7][3] = Queen('black', 7, 3, '\u2655')
            self[7][4] = self.blackKing
        else:
            self[7][4] = Queen('black', 7, 4, '\u2655')
            self[7][3] = self.blackKing


        self.save_pieces()

        if self.game_mode != 0:
            self.reverse()

    def save_pieces(self):
        for i in range(8):
            for j in range(8):
                if isinstance(self[i][j], ChessPiece):
                    if self[i][j].color == 'white':
                        self.whites.append(self[i][j])
                    else:
                        self.blacks.append(self[i][j])

    def make_move(self, piece, x, y, keep_history=False):    # history is logged when ai searches for moves
        global white_king_has_moved
        #If it is the white king
        if piece.unicode == '\u265A':
            #If it is moving to the castle square and it is still standing on the original square
            if x == 0 and y == 6 and piece.x == 0 and piece.y == 4:
                self.make_move(self[0][7], 0, 5, keep_history=True)
            if x == 0 and y == 2 and piece.x == 0 and piece.y == 4:
                self.make_move(self[0][0], 0, 3, keep_history=True)
            white_king_has_moved.append(True)
        #If it is the black king
        if piece.unicode == '\u2654':
            #If it is moving to the castle square and it is still standing on the original square
            if x == 0 and y == 1 and piece.x == 0 and piece.y == 3:
                self.make_move(self[0][0], 0, 2, keep_history=True)
            if x == 0 and y == 5 and piece.x == 0 and piece.y == 3:
                self.make_move(self[0][7], 0, 4, keep_history=True)
            black_king_gm1_has_moved.append(True)

        #If it a white rook
        if piece.unicode == '\u265C':
            #If it is the rook standing in the right corner
            if piece.x == 0 and piece.y == 7:
                white_rook_gm0_right_has_moved.append(True)
            if piece.x == 0 and piece.y == 0:
                white_rook_gm0_left_has_moved.append(True)

        #If it a black rook
        if piece.unicode == '\u2656':
            #If it is the rook standing in the right corner
            if piece.x == 0 and piece.y == 0:
                black_rook_gm1_left_has_moved.append(True)
            if piece.x == 0 and piece.y == 7:
                black_rook_gm1_right_has_moved.append(True)


        old_x = piece.x
        old_y = piece.y
        if keep_history:
            self.board[old_x][old_y].set_last_eaten(self.board[x][y])
        else:
            if isinstance(self.board[x][y], ChessPiece):
                if self.board[x][y].color == 'white':
                    self.whites.remove(self.board[x][y])
                else:
                    self.blacks.remove(self.board[x][y])
        self.board[x][y] = self.board[old_x][old_y]
        self.board[old_x][old_y] = 'empty-block'
        self.board[x][y].set_position(x, y, keep_history)

    def unmake_move(self, piece):
        global white_king_has_moved
        x = piece.x
        y = piece.y


        self.board[x][y].set_old_position()
        old_x = piece.x
        old_y = piece.y
        #If it is the white king
        if piece.unicode == '\u265A':
            white_king_has_moved.pop()
            #If it was standing on the castle square
            if x == 0 and y == 6:
                #If there is pieces standing on the castle squares
                if self[0][4] != 'empty-block' and self[0][5] != 'empty-block':
                    #If the pieces standing there are the king and rook
                    if self[0][5].unicode == '\u265C' and self[0][6].unicode == '\u265A':
                        #If it moving back to the kings square
                        if old_x == 0 and old_y == 4:
                            self.unmake_move(self[0][5])
            if x == 0 and y == 2:
                #If there is pieces standing on the castle squares
                if self[0][3] != 'empty-block' and self[0][2] != 'empty-block':
                    #If the pieces standing there are the king and rook
                    if self[0][3].unicode == '\u265C' and self[0][2].unicode == '\u265A':
                        #If it moving back to the kings square
                        if old_x == 0 and old_y == 4:
                            self.unmake_move(self[0][3])

        #If it is the black king
        if piece.unicode == '\u2654':
            black_king_gm1_has_moved.pop()
            #If it was standing on the castle square
            if x == 0 and y == 1:
                #If there is pieces standing on the castle squares
                if self[0][1] != 'empty-block' and self[0][2] != 'empty-block':
                    #If the pieces standing there are the king and rook
                    if self[0][1].unicode == '\u2654' and self[0][2].unicode == '\u2656':
                        #If it moving back to the kings square
                        if old_x == 0 and old_y == 3:
                            self.unmake_move(self[0][2])
            elif x == 0 and y == 5:
                #If there is pieces standing on the castle squares
                if self[0][4] != 'empty-block' and self[0][5] != 'empty-block':
                    #If the pieces standing there are the king and rook
                    if self[0][5].unicode == '\u2654' and self[0][4].unicode == '\u2656':
                        #If it moving back to the kings square
                        if old_x == 0 and old_y == 3:
                            self.unmake_move(self[0][4])

        #If it is the white rook
        if piece.unicode == '\u265C':
            if old_x == 0 and old_y == 7:
                white_rook_gm0_right_has_moved.pop()
            if old_x == 0 and old_y == 0:
                white_rook_gm0_left_has_moved.pop()

        #If it is the black rook
        if piece.unicode == '\u2656':
            if old_x == 0 and old_y == 0:
                black_rook_gm1_left_has_moved.pop()
            if old_x == 0 and old_y == 7:
                black_rook_gm1_right_has_moved.pop()

        self.board[old_x][old_y] = self.board[x][y]
        self.board[x][y] = piece.get_last_eaten()


    def reverse(self):
        self.board = self.board[::-1]
        for i in range(8):
            for j in range(8):
                if isinstance(self.board[i][j], ChessPiece):
                    piece = self.board[i][j]
                    piece.x = i
                    piece.y = j

    def __getitem__(self, item):
        return self.board[item]

    def has_opponent(self, piece, x, y):
        if not self.is_valid_move(x, y):
            return False
        if isinstance(self.board[x][y], ChessPiece):
            return piece.color != self[x][y].color
        return False

    def has_friend(self, piece, x, y):
        if not self.is_valid_move(x, y):
            return False
        if isinstance(self[x][y], ChessPiece):
            return piece.color == self[x][y].color
        return False

    @staticmethod
    def is_valid_move(x, y):
        return 0 <= x < 8 and 0 <= y < 8

    def has_empty_block(self, x, y):
        if not self.is_valid_move(x, y):
            return False
        return not isinstance(self[x][y], ChessPiece)

    def get_player_color(self):
        if self.game_mode == 0:
            return 'white'
        return 'black'

    def king_is_threatened(self, color, move=None):
        if color == 'white':
            enemies = self.blacks
            king = self.whiteKing
        else:
            enemies = self.whites
            king = self.blackKing
        threats = []
        for enemy in enemies:
            moves = enemy.get_moves(self)
            if (king.x, king.y) in moves:
                threats.append(enemy)
        if move and len(threats) == 1 and threats[0].x == move[0] and threats[0].y == move[1]:
            return False
        return True if len(threats) > 0 else False

    def is_terminal(self):
        terminal1 = self.white_won()
        terminal2 = self.black_won()
        terminal3 = self.draw()
        return terminal1 or terminal2 or terminal3

    def draw(self):
        if not self.king_is_threatened('white') and not self.has_moves('white'):
            return True
        if not self.king_is_threatened('black') and not self.has_moves('black'):
            return True
        if self.insufficient_material():
            return True
        return False

    def white_won(self):
        if self.king_is_threatened('black') and not self.has_moves('black'):
            return True
        return False

    def black_won(self):
        if self.king_is_threatened('white') and not self.has_moves('white'):
            return True
        return False

    def has_moves(self, color):
        total_moves = 0
        for i in range(8):
            for j in range(8):
                if isinstance(self[i][j], ChessPiece) and self[i][j].color == color:
                    piece = self[i][j]
                    total_moves += len(piece.filter_moves(piece.get_moves(self), self))
                    if total_moves > 0:
                        return True
        return False

    def insufficient_material(self):
        total_white_knights = 0
        total_black_knights = 0
        total_white_bishops = 0
        total_black_bishops = 0
        total_other_white_pieces = 0
        total_other_black_pieces = 0

        for piece in self.whites:
            if piece.type == 'Knight':
                total_white_knights += 1
            elif piece.type == 'Bishop':
                total_white_bishops += 1
            elif piece.type != 'King':
                total_other_white_pieces += 1

        for piece in self.blacks:
            if piece.type == 'Knight':
                total_black_knights += 1
            elif piece.type == 'Bishop':
                total_black_bishops += 1
            elif piece.type != 'King':
                total_other_black_pieces += 1

        weak_white_pieces = total_white_bishops + total_white_knights
        weak_black_pieces = total_black_bishops + total_black_knights

        if self.whiteKing and self.blackKing:
            if weak_white_pieces + total_other_white_pieces + weak_black_pieces + total_other_black_pieces == 0:
                return True
            if weak_white_pieces + total_other_white_pieces == 0:
                if weak_black_pieces == 1:
                    return True
            if weak_black_pieces + total_other_black_pieces == 0:
                if weak_white_pieces == 1:
                    return True
            if len(self.whites) == 1 and len(self.blacks) == 16 or len(self.blacks) == 1 and len(self.whites) == 16:
                return True
            if total_white_knights == weak_white_pieces + total_other_white_pieces and len(self.blacks) == 1:
                return True
            if total_black_knights == weak_black_pieces + total_other_black_pieces and len(self.whites) == 1:
                return True
            if weak_white_pieces == weak_black_pieces == 1 and total_other_white_pieces == total_other_black_pieces == 0:
                return True

    def evaluate(self):
        white_points = 0
        black_points = 0
        #i = vertical starting from bottom 0
        #j = horizontal
        for i in range(8):
            for j in range(8):
                if isinstance(self[i][j], ChessPiece):
                    piece = self[i][j]
                    if piece.color == 'white':
                        if i == 4:
                            white_points += 1
                        #white_points += 4 - abs(i - 4)
                        white_points += 4 - abs(j - 4)

                        #if j == 4:
                         #   white_points += 1
                        white_points += piece.get_score()

                    else:
                        if i == 4:
                            black_points += 1
                        #black_points += 4 - abs(i - 4)
                        black_points += 4 - abs(j - 4)

                        #if j == 4:
                         #   black_points += 1
                        black_points += piece.get_score()
        if self.get_player_color() == "white":
            return black_points - white_points
        return white_points - black_points

    def __str__(self):
        return str(self[::-1]).replace('], ', ']\n')

    def __repr__(self):
        return 'Board'

    def unicode_array_repr(self):
        data = deepcopy(self.board)
        for idx, row in enumerate(self.board):
            for i, p in enumerate(row):
                if isinstance(p, ChessPiece):
                    un = p.unicode
                else:
                    un = '\u25AF'
                data[idx][i] = un
        return data[::-1]

    def get_king(self, piece):
        if piece.color == 'white':
            return self.whiteKing
        return self.blackKing

    def specific_castle(self,board,color,long,king_square,rook_square,short_square1=False,short_square2=False, long_square1=False,long_square2=False,long_square3=False):
        #If player is white and on the bottom
        if color == "white":
                #If there is a piece on the kings square and rooks sqaure
            if self.board[king_square[0]][king_square[1]] != 'empty-block' and self.board[rook_square[0]][rook_square[1]] != 'empty-block':
                    #If the pieces are a king and a rook, and the squares in between are empty
                if not long:
                    if self.board[king_square[0]][king_square[1]].unicode == '\u265A' and self.board[rook_square[0]][rook_square[1]].unicode == '\u265C' and self.board[short_square1[0]][short_square1[1]] == 'empty-block' and self.board[short_square2[0]][short_square2[1]] == 'empty-block':
                            # If neither the king or rook has moved
                        if not white_king_has_moved[-1] and not white_rook_gm0_right_has_moved[-1]:
                                # If the king is not in check
                            if self.king_is_threatened(color) == False:

                                self.make_move(self.whiteKing, short_square1[0], short_square1[1], keep_history=True)
                                    # If the square next to is not threatened
                                if self.king_is_threatened(color, (short_square1[0], short_square1[1])) == False:
                                    self.unmake_move(self.whiteKing)
                                    return True
                                self.unmake_move(self.whiteKing)
                else:
                    if self.board[king_square[0]][king_square[1]].unicode == '\u265A' and self.board[rook_square[0]][rook_square[1]].unicode == '\u265C' and self.board[long_square1[0]][long_square1[1]] == 'empty-block' and self.board[long_square2[0]][long_square2[1]] == 'empty-block' and self.board[long_square3[0]][long_square3[1]]== 'empty-block':
                        if not white_king_has_moved[-1] and not white_rook_gm0_left_has_moved[-1]:
                            if self.king_is_threatened(color) == False:
                                self.make_move(self.whiteKing, long_square1[0], long_square1[1], keep_history=True)
                                # If the square next to is not threatened
                                if self.king_is_threatened(color, (long_square1[0], long_square1[1])) == False:
                                    self.unmake_move(self.whiteKing)
                                    return True
                                self.unmake_move(self.whiteKing)
        elif color == "black":
            if self.board[king_square[0]][king_square[1]] != 'empty-block' and self.board[rook_square[0]][rook_square[1]] != 'empty-block':
                    # If the pieces are a king and a rook, and the squares in between are empty
                if not long:
                    if self.board[king_square[0]][king_square[1]].unicode == '\u2654' and \
                            self.board[rook_square[0]][rook_square[1]].unicode == '\u2656' and \
                            self.board[short_square1[0]][short_square1[1]] == 'empty-block' and \
                            self.board[short_square2[0]][short_square2[1]] == 'empty-block':
                            # If neither the king or rook has moved
                        if not black_king_gm1_has_moved[-1] and not black_rook_gm1_left_has_moved[-1]:
                                # If the king is not in check
                            if self.king_is_threatened(color) == False:

                                self.make_move(self.blackKing, short_square1[0], short_square1[1],keep_history=True)
                                    # If the square next to is not threatened
                                if self.king_is_threatened(color, (short_square1[0], short_square1[1])) == False:
                                    self.unmake_move(self.blackKing)
                                    return True
                                self.unmake_move(self.blackKing)
                else:
                    if self.board[king_square[0]][king_square[1]].unicode == '\u2654' and \
                            self.board[rook_square[0]][rook_square[1]].unicode == '\u2656' and \
                            self.board[long_square1[0]][long_square1[1]] == 'empty-block' and \
                            self.board[long_square2[0]][long_square2[1]] == 'empty-block' and \
                            self.board[long_square3[0]][long_square3[1]] == 'empty-block':
                        if not black_king_gm1_has_moved[-1] and not black_rook_gm1_right_has_moved[-1]:
                            if self.king_is_threatened(color) == False:
                                self.make_move(self.blackKing, long_square1[0], long_square1[1], keep_history=True)
                                    # If the square next to is not threatened
                                if self.king_is_threatened(color, (long_square1[0], long_square1[1])) == False:
                                    self.unmake_move(self.blackKing)
                                    return True
                                self.unmake_move(self.blackKing)

    def has_castling(self,board,color):
        moves = []
        if color == "white":
            if self.specific_castle(board,color,False,(0,4),(0,7),short_square1=(0,5),short_square2=(0,6)):
                moves.append((0,6))
            if self.specific_castle(board,color,True,(0,4),(0,0),long_square1=(0,1),long_square2=(0,2),long_square3=(0,3)):
                moves.append((0,2))
            #if self.specific_castle(board,color,False,(7,3),(7,0),short_square1=(7,1),short_square2=(7,2)):
             #   moves.append((7,1))
            #if self.specific_castle(board,color,True,(7,3),(7,7),long_square1=(7,4),long_square2=(7,5),long_square3=(7,6)):
              #  moves.append((7,5))
        else:
            if self.specific_castle(board,color,False,(0,3),(0,0),short_square1=(0,1),short_square2=(0,2)):
                moves.append((0,1))
            if self.specific_castle(board,color,True,(0,3),(0,7),long_square1=(0,4),long_square2=(0,5),long_square3=(0,6)):
                moves.append((0,5))
            #if self.specific_castle(board,color,False,(7,3),(7,0),short_square1=(7,1),short_square2=(7,2)):
             #   moves.append((7,1))
            #if self.specific_castle(board,color,True,(7,3),(7,7),long_square1=(7,4),long_square2=(7,5),long_square3=(7,6)):
             #   moves.append((7,5))

        return moves



