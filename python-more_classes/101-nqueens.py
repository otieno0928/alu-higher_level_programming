#!/usr/bin/python3
"""
N Queens Problem Solver
Solves the challenge of placing N non-attacking queens on an N x N chessboard.
"""
import sys


def is_safe(board, row, col):
    """Check if a queen can be placed on board[row][col]."""
    for r, c in board:
        if c == col or abs(r - row) == abs(c - col):
            return False
    return True


def solve_nqueens(board, row, n):
    """Recursively solve the N queens problem using backtracking."""
    if row == n:
        print(board)
        return

    for col in range(n):
        if is_safe(board, row, col):
            board.append([row, col])
            solve_nqueens(board, row + 1, n)
            board.pop()


def main():
    """Main function to parse arguments and initiate the solution."""
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    solve_nqueens([], 0, n)


if __name__ == "__main__":
    main()
