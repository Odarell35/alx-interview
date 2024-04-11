#!/usr/bin/python3
"""Module"""
import sys

def is_safe(board, row, col, n):
    """Check if there is a queen in the same column"""
    for i in range(row):
        if board[i][col] == 'Q':
            return False
    
    # Check upper left diagonal
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 'Q':
            return False
    
    # Check upper right diagonal
    for i, j in zip(range(row, -1, -1), range(col, n)):
        if board[i][j] == 'Q':
            return False
    
    return True

def solve_nqueens(board, row, n):
    """solve """
    if row == n:
        for r in board:
            print(''.join(r))
        print()
        return
    
    for col in range(n):
        if is_safe(board, row, col, n):
            board[row][col] = 'Q'
            solve_nqueens(board, row + 1, n)
            board[row][col] = '.'

def nqueens(N):
    """method"""
    try:
        N = int(N)
    except ValueError:
        sys.exit(1)
    
    if N < 4:
        sys.exit(1)
    
    board = [['.' for _ in range(N)] for _ in range(N)]
    solve_nqueens(board, 0, N)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    
    nqueens(sys.argv[1])


