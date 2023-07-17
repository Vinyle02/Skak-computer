import math
from Board import Board
from ChessPiece import *
import graphics
import time
import Minimax_V3
import MinimaxV2
from functools import wraps
from Logger import Logger, BoardRepr
import random


positions_evaluated = 0
turn = 0

def minimax(board, depth,max_player, alpha, beta, save_move=False,):
    global positions_evaluated
    if depth == 0:
        return [[0,0,0]]
    data = []


    if max_player:
        max_eval = -900000000000
        for i in range(8):
            for j in range(8):
                if isinstance(board[i][j], ChessPiece) and board[i][j].color != board.get_player_color():
                    piece = board[i][j]
                    moves = piece.get_moves(board)
                    if moves:
                        for move in moves:

                            board.make_move(piece, move[0], move[1], True)
                            mini = minimax(board, depth - 1, False, alpha, beta)

                            enemy_data = mini[0][2]
                            evaluation = board.evaluate() + enemy_data

                            if evaluation > max_eval:

                                data.clear()
                                data.append([piece,move,evaluation,mini[0][0],mini[0][1]])

                           # elif evaluation == max_eval:
                           #     data.append([piece,move,evaluation,mini[0][0],mini[0][1]])
                            max_eval = max(max_eval, evaluation)
                            positions_evaluated += 1
                            board.unmake_move(piece)
                            alpha = max(alpha, max_eval)
                            if beta <= alpha:
                                break
        return data
    else:
        min_eval = 9000000000

        for i in range(8):
            for j in range(8):
                if isinstance(board[i][j], ChessPiece) and board[i][j].color == board.get_player_color():
                    piece = board[i][j]
                    moves = piece.get_moves(board)
                    if moves:
                        for move in moves:

                            board.make_move(piece, move[0], move[1], True)
                            mini = minimax(board, depth-1,True, alpha, beta)

                            enemy_data = mini[0][2]
                            evaluation = board.evaluate() + enemy_data

                            if evaluation <= min_eval:
                                data.clear()
                                data.append([piece,move,evaluation,mini[0][0],mini[0][1]])
                           # elif evaluation == min_eval:
                            #    data.append([piece,move,evaluation,mini[0][0],mini[0][1]])
                            min_eval = min(min_eval, evaluation)
                            positions_evaluated += 1
                            board.unmake_move(piece)
                            beta = min(beta, min_eval)
                            if beta <= alpha:
                                break
        return data

def get_sorted_moves(board, maximising):
    moves = []
    for i in range(8):
        for j in range(8):
            piece = board[i][j]
            if isinstance(piece, ChessPiece) and ((maximising and piece.color != board.get_player_color()) or
                                                  (not maximising and piece.color == board.get_player_color())):
                for move in piece.get_moves(board):
                    board.make_move(piece, move[0], move[1], True)  # Make the move
                    score = board.evaluate()
                    moves.append((score, piece, move))
                    board.unmake_move(piece)  # Undo the move

    # Sort the moves in descending order of score if maximising player, and ascending if minimising
    moves.sort(key=lambda x: x[0], reverse=maximising)
    return moves


def get_ai_move(board):
    global turn
    global positions_evaluated
    start = time.perf_counter()
    print("Loading moves...")
    board.has_castling(board,"white")
    data = MinimaxV2.minimax(board,4,True, -10000, 10000)
    random_move = 0
    #if len(data) > 1:
     #   random_move = random.randint(0,len(data)-1)
      #  print(data[0][2])
     #   print(data[random_move][2])
    #if data[0][2] > data[random_move][2]:
        #random_move = 0

    piece = data[random_move][0]
    best_move = data[random_move][1]
    if board.get_player_color() == "white":
        column = chr(best_move[1]+97)
        row = best_move[0]+1
    else:
        column = chr(abs(best_move[1]-7)+97)
        row = abs(best_move[0]-8)
    end = time.perf_counter()
    time_taken = round(end-start,2)
    #print(f"Data: {data}")
    print("Time: " + str(time_taken) + " seconds taken")
    #print(str(piece) + " moved to " + str(column) + "," + str(row))
    #print("Best move val: " + str(data[random_move][2]))
    print("Positions evaluated: " + str(positions_evaluated))
    positions_evaluated = 0

    if data[random_move][2] < -10000:
        graphics.game_over = True
        graphics.game_over_txt = 'WHITE WINS!'
    elif data[random_move][2] > 10000:
        graphics.game_over = True
        graphics.game_over_txt = 'BLACK WINS!'
    else:
        board.make_move(piece,best_move[0],best_move[1])
    print(f"Computer best move: {data[random_move][3]} moving to {data[random_move][4]}")
    print(f"Actual best move: {minimax(board,3,False, -10000, 10000)[0][:2]}")
    #print(f"The board is the same: {board == data[random_move][5]}")
    #print(data[random_move][5])
    turn += 1



def get_random_move(board):
    pass

def get_ai_move2(board):
    global turn
    global positions_evaluated
    start = time.perf_counter()
    print("Loading moves...")
    board.has_castling(board,"white")
    data = Minimax_V3.minimax(board,4,True, -10000, 10000, True, [[],0])
    sorted_list = sorted(data[0], key=lambda x: x[2], reverse=True)
    random_move = 0
    #if len(data) > 1:
     #   random_move = random.randint(0,len(data)-1)
      #  print(data[0][2])
     #   print(data[random_move][2])
    #if data[0][2] > data[random_move][2]:
        #random_move = 0

    piece = sorted_list[random_move][0]
    best_move = sorted_list[random_move][1]
    #if board.get_player_color() == "white":
     #   column = chr(best_move[1]+97)
      #  row = best_move[0]+1
    #else:
     #   column = chr(abs(best_move[1]-7)+97)
      #  row = abs(best_move[0]-8)
    end = time.perf_counter()
    time_taken = round(end-start,2)
    #print(f"Data: {data}")
    print("Time: " + str(time_taken) + " seconds taken")
    #print(str(piece) + " moved to " + str(column) + "," + str(row))
    #print("Best move val: " + str(data[random_move][2]))
    print("Positions evaluated: " + str(positions_evaluated))
    positions_evaluated = 0

    if data[1] < -10000:
        graphics.game_over = True
        graphics.game_over_txt = 'WHITE WINS!'
    elif data[1] > 10000:
        graphics.game_over = True
        graphics.game_over_txt = 'BLACK WINS!'
    else:
        board.make_move(piece,best_move[0],best_move[1])
    #print(f"Computer best move: {data[random_move][3]} moving to {data[random_move][4]}")
    #print(f"Actual best move: {minimax(board,3,False, -10000, 10000)[0][:2]}")
    #print(f"The board is the same: {board == data[random_move][5]}")
    #print(data[random_move][5])
    turn += 1