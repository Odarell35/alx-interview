#!/usr/bin/python3
"""Module"""
import sys


def is_safe(board, row, col):
    """Check if there is a queen in the same column"""
    for i in range(row):
        if board[i] == col:
            return False
        # Check diagonals
        if abs(board[i] - col) == abs(i - row):
            return False
    return True


def solve_nqueens_util(board, row, n, solutions):
    """method"""
    if row == n:
        solutions.append(board[:])
        return

    for col in range(n):
        if is_safe(board, row, col):
            board[row] = col
            solve_nqueens_util(board, row + 1, n, solutions)
            board[row] = -1


def solve_nqueens(n):
    """method"""
    if not n.isdigit():
        print("N must be a number")
        sys.exit(1)

    n = int(n)
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = [-1] * n
    solutions = []
    solve_nqueens_util(board, 0, n, solutions)

    for solution in solutions:
        print([[i, solution[i]] for i in range(n)])


if __name__ == "__main__":
    """run main"""
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    solve_nqueens(sys.argv[1])

    nqueens(sys.argv[1])


