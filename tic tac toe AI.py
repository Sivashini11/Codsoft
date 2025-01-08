import math

def print_board(board):
    for row in board: print(" | ".join(row)); print("-" * 5)

def check_winner(board):
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != ' ' or board[0][i] == board[1][i] == board[2][i] != ' ': return board[i][i]
    if board[0][0] == board[1][1] == board[2][2] != ' ' or board[0][2] == board[1][1] == board[2][0] != ' ': return board[1][1]
    return 'Draw' if all(cell != ' ' for row in board for cell in row) else None

def minimax(board, depth, is_max, alpha=-math.inf, beta=math.inf):
    result = check_winner(board)
    if result: return {'X': -10, 'O': 10, 'Draw': 0}[result] + (-depth if result == 'X' else depth)
    eval_fn = max if is_max else min; best_eval = -math.inf if is_max else math.inf
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                board[i][j] = 'O' if is_max else 'X'
                eval_val = minimax(board, depth + 1, not is_max, alpha, beta)
                board[i][j] = ' '
                best_eval = eval_fn(best_eval, eval_val)
                if is_max: alpha = max(alpha, best_eval)
                else: beta = min(beta, best_eval)
                if beta <= alpha: break
    return best_eval

def best_move(board):
    move, best_val = (-1, -1), -math.inf
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                board[i][j] = 'O'
                move_val = minimax(board, 0, False)
                board[i][j] = ' '
                if move_val > best_val: move, best_val = (i, j), move_val
    return move

def main():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    print("You are X, AI is O.")
    while True:
        print_board(board)
        result = check_winner(board)
        if result: print(f"{result} wins!" if result != 'Draw' else "It's a draw!"); break
        try:
            row, col = map(int, input("Your move (row col): ").split())
            if board[row][col] != ' ': print("Taken. Try again."); continue
            board[row][col] = 'X'
        except: print("Invalid input. Use 0-2."); continue
        if not check_winner(board):
            ai_move = best_move(board)
            board[ai_move[0]][ai_move[1]] = 'O'

if __name__ == "__main__": main()
