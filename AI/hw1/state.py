'''
Homework #1 | Yuval Mashiah, 329245161
--------------------------------------------------------

The Heuristic:
Let K be the total number of lights currently turned ON in the grid. 
The heuristic function h(n) calculates the minimum possible number of clicks required by dividing K by 5 
and rounding up to the nearest whole number.

The Proof:
- Definition: N = h(n) = ceil(K/5)
To prove that a heuristic is admissible for the A* algorithm, I must demonstrate that it never 
overestimates the true cost (the actual minimum number of moves) required to reach the target state, 
which is a completely dark board.
In the game of Lights Out, a single click toggles the state of the selected square and its immediate 
orthogonal neighbors (up, down, left, and right). This means a single move can affect a maximum of 5 squares.
Suppose the current board state has exactly K lights ON. The absolute best-case scenario—the most efficient 
mathematical path possible—would be if every single click turned off exactly 5 lights, without ever 
accidentally turning a dark square back on.Under this perfect (and often physically impossible) scenario, 
it would take exactly N moves to clear the board.
Because it is strictly impossible within the rules of the game to turn off K lights in fewer than N moves, 
our heuristic value will always be less than or equal to the actual number of moves required.
Conclusion:
Since h(n) equals to or less than true_cost(n) for every possible state, the heuristic never overestimates 
the distance to the goal and is therefore strictly admissible.
'''

import random
import math

def create(n):
    # Create an nXn board initialized to 0 (all lights off)
    board = [[0 for _ in range(n)] for _ in range(n)]
    
    # To ensure the board is solvable, make a series of random valid clicks.
    # Since clicking the same square twice reverts it to its previous state,
    # a number of random clicks equal to the board size squared is enough to shuffle it well.
    for _ in range(n * n):
        r = random.randrange(n)
        c = random.randrange(n)
        toggle(board, r, c)
        
    return [board, ""]

def toggle(board, r, c):
    # Helper function to toggle the state of a square and its 4 orthogonal neighbors
    n = len(board)
    directions = [(0, 0), (-1, 0), (1, 0), (0, -1), (0, 1)]
    for dr, dc in directions:
        nr, nc = r + dr, c + dc
        if 0 <= nr < n and 0 <= nc < n:
            board[nr][nc] = 1 - board[nr][nc]

def get_next(x):
    ns = []
    board = x[0]
    path = x[1]
    n = len(board)
    
    # Extract the position of the last click to enforce lexicographical order 
    # (prevents cycles and duplicates in the search tree)
    last_r, last_c = -1, -1
    if path != "":
        # The path string consists of moves like "(0,2)(1,1)"
        last_move = path.split('(')[-1] # Will return "1,1)"
        last_r = int(last_move.split(',')[0])
        last_c = int(last_move.split(',')[1].split(')')[0])
    
    for r in range(n):
        for c in range(n):
            # In this game, the order of clicks doesn't matter. Therefore, to avoid expanding 
            # both "(0,1)(1,1)" and "(1,1)(0,1)", we only allow clicks that come 'after' 
            # the last click in the grid (lexicographically).
            if (r > last_r) or (r == last_r and c > last_c):
                
                # Create a deep copy of the 2D board
                new_board = [[val for val in row] for row in board]
                
                # Execute the click
                toggle(new_board, r, c)
                
                # Create the new move string
                move_str = f"({r},{c})"
                
                ns.append([new_board, path + move_str])
    return ns

def path_len(x):
    # Since every move adds an opening parenthesis '(', counting them equals the number of clicks.
    return x[1].count('(')

def is_target(x):
    # Check if all squares in all rows are turned off (equal to 0)
    for row in x[0]:
        if 1 in row:
            return False
    return True

def hdistance(s):
    # Calculate the total number of squares that are currently ON
    lights_on = sum(row.count(1) for row in s[0])
    
    # Divide by 5 and round up. Adding 4 and performing integer division by 5 
    # is an efficient way to do math.ceil without floating-point conversion.
    return (lights_on + 4) // 5