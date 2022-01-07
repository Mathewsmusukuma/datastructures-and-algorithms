
def game_of_life(board):
    """
    Do not return anything, modify board in-place instead.
    """
    
    ROWS, COLS = len(board), len(board[0])

    def count_neighbor(r, c):
        neighbor = 0
        for i in range(r - 1, r + 2):
            for j in range(c - 1, c + 2):
                if ((i == r and j == c) or i < 0 or j < 0 \
                    or i == ROWS or j == COLS):
                    continue
                if board[i][j] in [1, 3]:
                    neighbor += 1
        return neighbor

    for r in range(ROWS):
        for c in range(COLS):
            neighbor = count_neighbor(r, c)
            if board[r][c]:
                if neighbor in [2,3]:
                    board[r][c] = 3
            elif neighbor == 3:
                board[r][c] = 2
                    
    for r in range(ROWS):
        for c in range(COLS):
            if board[r][c] == 1:
                board[r][c] = 0
            elif board[r][c] in [2,3]:
                board[r][c] = 1
    
    return board


board = [[0,1,0],[0,0,1],[1,1,1],[0,0,0]]

res = game_of_life(board)
print(res)
