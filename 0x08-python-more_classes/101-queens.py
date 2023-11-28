#!/usr/bin/python3
"""program that solves the N queens problem"""

import sys


def is_safe(board, row, col, n):
    """checks if there is a queen in the same row"""
    for i in range(col):
        if board[row][i] == 1:
            return False

    """checks upper diagonal on left side"""
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    """checks lower diagonal on left side"""
    for i, j in zip(range(row, n, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True


def solve_nqueens_util(board, col, n, solutions):
    if col == n:
        """All queens are placed, print the solution"""
        solution = []
        for i in range(n):
            for j in range(n):
                if board[i][j] == 1:
                    solution.append([i, j])
        solutions.append(solution)
        return

    for i in range(n):
        if is_safe(board, i, col, n):
            board[i][col] = 1
            solve_nqueens_util(board, col + 1, n, solutions)
            board[i][col] = 0


def solve_nqueens(n):
    """checks if N is at least 4"""
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    """initialize the chessboard"""
    board = [[0 for _ in range(n)] for _ in range(n)]

    """store solutions in a list"""
    solutions = []

    """start with the first column"""
    solve_nqueens_util(board, 0, n, solutions)

    """sort solutions before printing"""
    solutions.sort()
    for solution in solutions:
        print(solution)


if __name__ == "__main__":
    """checks the number of arguments"""
    if len(sys.argv) != 2:
        print("Usage: {} N".format(sys.argv[0]))
        sys.exit(1)

    try:
        """parse N from the command line argument"""
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    solve_nqueens(N)
