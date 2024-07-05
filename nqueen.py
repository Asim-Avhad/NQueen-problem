def solve_n_queen(n):
    def can_place(board, row, col):
        for i in range(col):
            if board[row][i] == 1:
                return False
        for i, j in zip(range(row, -1, -1) , range(col, -1, -1)):
            if board[i][j] == 1:
                return False
        for i, j in zip(range(row, n, 1), range(col, -1, -1)):
            if board[i][j] == 1:
                return False
        return True
    
    def solve(board, col):
        if col >= n:
            print_board(board)
            print("\n")
        for i in range(n):
            if can_place(board, i, col):
                board[i][col] = 1
                solve(board, col + 1)
                board[i][col] = 0
        
    def create_board(n):
        board = [[0] * n for i in range(n)]
        solve(board, 0)
    
    def print_board(board):
        for i in range(n):
            for j in range(n):
                print(board[i][j], end = " ")
            print()
    create_board(n)

while True:
    num_queens = int(input("Enter the number of queens:"))
    if num_queens == 2:
        print("Unsolvable")
    elif num_queens == 3:
        print("Unsolvable")
    else:
        solve_n_queen(num_queens)