import os
import random

def initialize_honeycomb(rows, cols, honey_count, obstacle_count):
    """
    Initialize the honeycomb with random honey spots and obstacles.
    """
    honeycomb = [['-' for _ in range(cols)] for _ in range(rows)]
    # Randomly place honey spots
    for _ in range(honey_count):
        honey_row, honey_col = random.randint(0, rows - 1), random.randint(0, cols - 1)
        honeycomb[honey_row][honey_col] = 'H'

    # Randomly place obstacles
    for _ in range(obstacle_count):
        obstacle_row, obstacle_col = random.randint(0, rows - 1), random.randint(0, cols - 1)
        # Ensure obstacle does not overlap with honey or other obstacles
        while honeycomb[obstacle_row][obstacle_col] != '-':
            obstacle_row, obstacle_col = random.randint(0, rows - 1), random.randint(0, cols - 1)
        honeycomb[obstacle_row][obstacle_col] = 'X'

    return honeycomb

def print_honeycomb(honeycomb, bee_position, score, level):
    """
    Print the honeycomb structure with the bee, honey, obstacles, score, and level.
    """
    rows, cols = len(honeycomb), len(honeycomb[0])
    display = f"Score: {score} | Level: {level}\n"
    for row in range(rows):
        line = ''
        for col in range(cols):
            if (row, col) == bee_position:
                cell = 'B'
            else:
                cell = honeycomb[row][col]
            if row % 2 == 0:
                line += f" /{cell}\\ "
            else:
                line += f" \\{cell}/ "
        if row % 2 != 0:
            line = ' ' * 3 + line
        display += line + '\n'
    return display

def update_bee_position(bee_position, movement, rows, cols):
    """
    Update the bee's position based on the movement command.
    """
    new_row, new_col = bee_position
    if movement == 'W':
        new_row = max(0, bee_position[0] - 1)
    elif movement == 'A':
        new_col = max(0, bee_position[1] - 1)
    elif movement == 'S':
        new_row = min(rows - 1, bee_position[0] + 1)
    elif movement == 'D':
        new_col = min(cols - 1, bee_position[1] + 1)
    
    return new_row, new_col

def process_bee_action(honeycomb, bee_position, has_honey):
    """
    Process the action of the bee at its current position.
    """
    row, col = bee_position
    if honeycomb[row][col] == 'H' and not has_honey:
        has_honey = True  # Bee collects honey
        honeycomb[row][col] = '-'  # Remove honey from the cell
    elif honeycomb[row][col] == '-' and has_honey:
        has_honey = False  # Bee deposits honey
        honeycomb[row][col] = 'F'  # Mark cell as filled with honey

    return honeycomb, has_honey

