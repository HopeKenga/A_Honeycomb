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

