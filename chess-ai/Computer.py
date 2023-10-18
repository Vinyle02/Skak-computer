from ChessPiece import *
import time


positions_evaluated = 0
def add_pos():
    global positions_evaluated
    positions_evaluated += 1
depths_counted = 0
def count_depth():
    global depths_counted
    depths_counted += 1
turn = 1

def minimax(board, depth,max_player, alpha, beta):
    if depth == 0:
        return [0,0,0]
    data = []
    sorted_moves = get_sorted_moves(board, max_player)

    if max_player:
        max_eval = -900000000000
        for score, piece, move in sorted_moves:
            evaluation = board.evaluate_move(piece, piece.x, piece.y, move[0], move[1], piece.color)
            board.make_move(piece, move[0], move[1], True)
            mini = minimax(board, depth - 1, False, alpha, beta)
            enemy_data = mini[2]
            evaluation += enemy_data
            if evaluation > max_eval:
                data = [piece, move, evaluation]
            max_eval = max(max_eval, evaluation)
            add_pos()
            board.unmake_move(piece)
            alpha = max(alpha, max_eval)
            if beta <= alpha:
                break
    else:
        min_eval = 9000000000
        for score, piece, move in sorted_moves:
            evaluation = board.evaluate_move(piece, piece.x,piece.y,move[0],move[1],piece.color)
            board.make_move(piece, move[0], move[1], True)
            mini = minimax(board, depth-1,True, alpha, beta)

            enemy_data = mini[2]
            evaluation += enemy_data
            if evaluation <= min_eval:
                data = [piece,move,evaluation]
            min_eval = min(min_eval, evaluation)
            add_pos()
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
                    score = board.evaluate_move(piece, i, j, move[0], move[1], piece.color)
                    moves.append((score, piece, move))

    # Sort the moves in descending order of score if maximising player, and ascending if minimising
    moves.sort(key=lambda x: x[0], reverse= maximising)
    return moves


def get_ai_move(board):
    global turn
    global positions_evaluated
    start = time.perf_counter()
    print("Loading moves...")
    board.has_castling(board,"white")
    depth = 6
    data = minimax(board, depth, True, -10000, 10000)

    piece = data[0]
    best_move = data[1]
    if board.get_player_color() == "white":
        column = chr(best_move[1]+97)
        row = best_move[0]+1
    else:
        column = chr(abs(best_move[1]-7)+97)
        row = abs(best_move[0]-8)
    end = time.perf_counter()
    time_taken = round(end-start,2)
    print(f"Turn: {turn}")
    print(f"Time: {time_taken} seconds taken")
    print(f"{piece} moved to {column}, {row}")
    print(f"Positions evaluated: {positions_evaluated}")

    board.make_move(piece,best_move[0],best_move[1])
    positions_evaluated = 0
    turn += 1
