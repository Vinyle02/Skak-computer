import computer as pc

def minimax(board, depth,max_player, alpha, beta, save_move=False,):
    global positions_evaluated
    if depth == 0:
        return [[0,0,0]]
    data = []
    sorted_moves = pc.get_sorted_moves(board, max_player)

    if max_player:
        max_eval = -900000000000

        for score, piece, move in sorted_moves:
            board.make_move(piece, move[0], move[1], True)
            mini = minimax(board, depth - 1, False, alpha, beta)
            enemy_data = mini[0][2]
            evaluation = 0
            evaluation = board.evaluate()
            evaluation += enemy_data
            if evaluation > max_eval:

                data.clear()
                data.append([piece,move,evaluation,mini[0][0],mini[0][1]])

            elif evaluation == max_eval:
                data.append([piece,move,evaluation,mini[0][0],mini[0][1]])
            max_eval = max(max_eval, evaluation)
            board.unmake_move(piece)
            alpha = max(alpha, max_eval)
            if beta <= alpha:
                break
    else:
        min_eval = 9000000000
        for score, piece, move in sorted_moves:
            board.make_move(piece, move[0], move[1], True)
            mini = minimax(board, depth-1,True, alpha, beta)

            enemy_data = mini[0][2]
            evaluation = 0
            evaluation = board.evaluate()

            evaluation += enemy_data
            if evaluation <= min_eval:
                data.clear()
                data.append([piece,move,evaluation,mini[0][0],mini[0][1]])
            elif evaluation == min_eval:
                data.append([piece,move,evaluation,mini[0][0],mini[0][1]])
            min_eval = min(min_eval, evaluation)
            board.unmake_move(piece)
            beta = min(beta, min_eval)
            if beta <= alpha:
                break
    return data