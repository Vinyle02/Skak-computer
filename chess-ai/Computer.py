import math
from Board import Board
from ChessPiece import *
from functools import wraps
from Logger import Logger, BoardRepr
import random


def minimax(board, depth,max_player,current_data = None, alpha=False, beta=False, save_move=False,):

    if depth == 0:
        return [[0,0,0]]
    data = [[]]


    if max_player:
        max_eval = -90000
        for i in range(8):
            for j in range(8):
                if isinstance(board[i][j], ChessPiece) and board[i][j].color != board.get_player_color():
                    piece = board[i][j]
                    moves = piece.get_moves(board)
                    if moves:
                        for move in moves:
                            board.make_move(piece, move[0], move[1], True)
                            enemy_data = minimax(board, depth - 1, not max_player)[0][2]
                            evaluation = 0
                            evaluation += board.evaluate(True)
                            evaluation += enemy_data

                            if evaluation > max_eval:
                                data[0] = [piece,move,evaluation]
                            elif evaluation == max_eval:
                                data[0].append([piece,move,evaluation])
                            max_eval = max(max_eval, evaluation)
                            board.unmake_move(piece)
    else:
        min_eval = 90000

        for i in range(8):
            for j in range(8):
                if isinstance(board[i][j], ChessPiece) and board[i][j].color == board.get_player_color():
                    piece = board[i][j]
                    moves = piece.get_moves(board)
                    if moves:
                        for move in moves:

                            board.make_move(piece, move[0], move[1], True)
                            enemy_data = minimax(board, depth-1,not max_player)[0][2]

                            evaluation = 0
                            evaluation -= board.evaluate(False)
                            evaluation += enemy_data

                            if evaluation <= min_eval:
                                data[0] = [piece,move,evaluation]
                                min_eval = evaluation
                            board.unmake_move(piece)
    return data


def get_ai_move(board):
    data = minimax(board,3,True)
    print(len(data[0]))
    print("Best move val")
    print(data[0][2])

    piece = data[0][0]
    best_move = data[0][1]
    board.make_move(piece,best_move[0],best_move[1])


def get_random_move(board):
    pass
