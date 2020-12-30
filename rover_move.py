from typing import List


def rover_move(n: int, commands: List[str]) -> int:
    """
    A Mars rover is directed to move within a square matrix.
    It accepts a sequence of commands to move in any of the
    four directions from each cell: [UP, DOWN, LEFT or RIGHT].
    The rover starts from cell 0. and may not move diagonally
    or outside of the boundary.

    Args:
        n (int): square matrix size
        commands (List[str]): list of commands

    Returns:
        int: rover's final position
    """
    position_row = 0
    position_col = 0

    for command in commands:
        if command.lower() == "right":
            if position_col < n:
                position_col += 1
        elif command.lower() == "left":
            if position_col > 0:
                position_col -= 1
        elif command.lower() == "up":
            if position_row > 0:
                position_row -= 1
        elif command.lower() == "down":
            if position_row < n:
                position_row += 1

    return position_row * n + position_col


n1 = 4
commands1 = ["RIGHT", "UP", "DOWN", "LEFT", "DOWN", "DOWN"]
n2 = 4
commands2 = ["RIGHT", "DOWN", "LEFT", "LEFT", "DOWN"]
n3 = 5
commands3 = ["RIGHT", "DOWN", "LEFT", "LEFT", "DOWN"]
n4 = 5
commands4 = ["RIGHT", "DOWN", "LEFT", "LEFT", "DOWN", "RIGHT"]

assert rover_move(n1, commands1) == 12
assert rover_move(n2, commands2) == 8
assert rover_move(n3, commands3) == 10
assert rover_move(n4, commands4) == 11
