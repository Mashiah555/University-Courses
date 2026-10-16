'''
Homework #2 | Yuval Mashiah, 329245161
--------------------------------------------------------

Heuristic Strategy for Ultimate Tic-Tac-Toe:
Ultimate Tic-Tac-Toe requires evaluating both the 9x9 global board and the 3x3 macro-board.
Because the branching factor is immense (up to 81 possible moves initially), the heuristic must be 
computationally lightweight while strongly prioritizing macro-board control.

The heuristic calculates a score from the perspective of the COMPUTER (positive = good for Computer, negative = good for Human).
1. Macro-Board Evaluation: Winning a local board is the most critical step toward winning the game. 
   The algorithm evaluates the 3x3 macro-board just like a regular Tic-Tac-Toe board but multiplies the score by 100 times. 
   A potential line of 2 won boards for the computer is given a massive boost.
2. Local-Board Evaluation: For all local 3x3 boards that are still active, the algorithm calculates a standard 
   Tic-Tac-Toe heuristic (scoring potential lines of 1 or 2 marks). This acts as a tie-breaker, guiding 
   the algorithm to make optimal local moves when macro-board captures aren't immediately available.
3. Move Ordering Optimization: `getNext(s)` handles sorting the generated child states based on their 
   heuristic value. This ensures the Alpha-Beta Pruning algorithm explores the most promising paths first, 
   drastically increasing the number of branches pruned and preventing timeouts at high depths.
'''

import copy

VIC = 10**20      # The value of a winning board
LOSS = -VIC       # The value of a losing board
TIE = 0           # The value of a tie
SIZE = 3          # The length of a winning sequence
COMPUTER = SIZE+1 # Marks the computer's cells on the board
HUMAN = 1         # Marks the human's cells on the board
TIE_BOARD = 2     # Marks a local board that is full with no winner

'''
State representation for Ultimate Tic-Tac-Toe (list of 6 items):
s[0]: 9x9 game board - matrix (list of lists) of ints. Empty = 0.
s[1]: The heuristic value of the state. (0.00001 avoids conflict with TIE)
s[2]: Whose turn it is: HUMAN or COMPUTER.
s[3]: Number of empty cells remaining on the 9x9 board.
s[4]: 3x3 macro-board tracking won/tied local boards.
s[5]: Tuple (macro_r, macro_c) dictating where the next player MUST play. 
      If (-1, -1), the player can play in any active macro-board.
'''

def create():
    # Returns an empty board. The human plays first.
    board = [[0 for _ in range(9)] for _ in range(9)]
    macro_board = [[0 for _ in range(3)] for _ in range(3)]
    return [board, 0.00001, HUMAN, 81, macro_board, (-1, -1)]

def value(s):
    # Returns the heuristic value of s
    return s[1]

def printState(s):
    # Prints the 9x9 board with grid separators for clarity
    print("\n    0 1 2   3 4 5   6 7 8")
    for r in range(9):
        if r > 0 and r % 3 == 0:
            print("  " + "-" * 23)
        print(str(r) + " | ", end="")
        for c in range(9):
            if c > 0 and c % 3 == 0:
                print("| ", end="")
            
            val = s[0][r][c]
            if val == COMPUTER:
                print("X ", end="")
            elif val == HUMAN:
                print("O ", end="")
            else:
                print(". ", end="")
        print()
    print()
    
    # Print next move constraints
    req_mr, req_mc = s[5]
    if req_mr != -1 and not isFinished(s):
        print(f"--> Next move MUST be in the local board at ROW {req_mr}, COL {req_mc} (Cells: row {req_mr*3}-{req_mr*3+2}, col {req_mc*3}-{req_mc*3+2})")
    elif not isFinished(s):
        print("--> You can play in ANY available local board.")

    if value(s) == VIC:
        print("\nHa ha ha I won!")
    elif value(s) == LOSS:
        print("\nYou did it!")
    elif value(s) == TIE:
        print("\nIt's a TIE!")

def isFinished(s):
    # Returns True iff the game ended
    return s[1] in [LOSS, VIC, TIE]

def isHumTurn(s):
    # Returns True iff it is the human's turn to play
    return s[2] == HUMAN

def whoIsFirst(s):
    # The user decides who plays first
    try:
        ans = int(input("Who plays first? 1-me (Computer) / anything else-you (Human): "))
        if ans == 1:
            s[2] = COMPUTER
        else:
            s[2] = HUMAN
    except ValueError:
        s[2] = HUMAN

def isLegal(s, r, c):
    # Checks if a move at (r, c) on the 9x9 board is strictly legal
    if r < 0 or r >= 9 or c < 0 or c >= 9:
        return False
    if s[0][r][c] != 0: # Cell is already taken
        return False
    
    mr, mc = r // 3, c // 3
    if s[4][mr][mc] != 0: # The targeted local board is already won or full
        return False
        
    req_mr, req_mc = s[5]
    if req_mr != -1 and (req_mr != mr or req_mc != mc):
        return False # Move is not in the mandated local board
        
    return True

def evaluateGrid3x3(grid, r_offset=0, c_offset=0):
    # Evaluates a 3x3 grid (can be the macro-board or a sub-board)
    # Returns the winner (COMPUTER or HUMAN), TIE_BOARD if full, or 0 if active
    for i in range(3):
        # Rows
        if grid[r_offset + i][c_offset] == grid[r_offset + i][c_offset + 1] == grid[r_offset + i][c_offset + 2] and grid[r_offset + i][c_offset] in [COMPUTER, HUMAN]:
            return grid[r_offset + i][c_offset]
        # Cols
        if grid[r_offset][c_offset + i] == grid[r_offset + 1][c_offset + i] == grid[r_offset + 2][c_offset + i] and grid[r_offset][c_offset + i] in [COMPUTER, HUMAN]:
            return grid[r_offset][c_offset + i]
            
    # Diagonals
    if grid[r_offset][c_offset] == grid[r_offset + 1][c_offset + 1] == grid[r_offset + 2][c_offset + 2] and grid[r_offset][c_offset] in [COMPUTER, HUMAN]:
        return grid[r_offset][c_offset]
    if grid[r_offset + 2][c_offset] == grid[r_offset + 1][c_offset + 1] == grid[r_offset][c_offset + 2] and grid[r_offset + 2][c_offset] in [COMPUTER, HUMAN]:
        return grid[r_offset + 2][c_offset]

    # Check if full
    for r in range(3):
        for c in range(3):
            if grid[r_offset + r][c_offset + c] == 0:
                return 0 # Still active
    return TIE_BOARD

def scoreLine(c1, c2, c3):
    # Calculates heuristic score for a single row/col/diag
    counts = {COMPUTER: 0, HUMAN: 0, 0: 0, TIE_BOARD: 0}
    for cell in [c1, c2, c3]:
        counts[cell] = counts.get(cell, 0) + 1
        
    if counts[TIE_BOARD] > 0: return 0
    if counts[COMPUTER] > 0 and counts[HUMAN] > 0: return 0 # Blocked line
    
    if counts[COMPUTER] == 3: return 1000
    if counts[HUMAN] == 3: return -1000
    
    if counts[COMPUTER] == 2: return 10
    if counts[HUMAN] == 2: return -10
    
    if counts[COMPUTER] == 1: return 1
    if counts[HUMAN] == 1: return -1
    return 0

def calculateLinesScore(grid, r_offset=0, c_offset=0):
    # Sums heuristic scores for all rows, cols, and diags in a 3x3 grid
    score = 0
    for i in range(3):
        score += scoreLine(grid[r_offset + i][c_offset], grid[r_offset + i][c_offset + 1], grid[r_offset + i][c_offset + 2]) # Row
        score += scoreLine(grid[r_offset][c_offset + i], grid[r_offset + 1][c_offset + i], grid[r_offset + 2][c_offset + i]) # Col
    score += scoreLine(grid[r_offset][c_offset], grid[r_offset + 1][c_offset + 1], grid[r_offset + 2][c_offset + 2])         # Diag 1
    score += scoreLine(grid[r_offset + 2][c_offset], grid[r_offset + 1][c_offset + 1], grid[r_offset][c_offset + 2])         # Diag 2
    return score

def getHeuristicVal(s):
    # Computes total heuristic by combining macro-board dominance and local active boards
    h = 0
    macro = s[4]
    
    # 1. Macro board score (Highest Priority)
    h += calculateLinesScore(macro) * 100
    
    # 2. Local boards score (Secondary Priority)
    for mr in range(3):
        for mc in range(3):
            if macro[mr][mc] == 0: # Evaluate only active local boards
                h += calculateLinesScore(s[0], mr * 3, mc * 3)
                
    return h if h != 0 else 0.00001 # Ensure the return value won't accidentally be 0 (TIE)

def makeMove(s, r, c):
    # Executes the move, updates local/macro boards, calculates heuristic, and switches turns
    s[0][r][c] = s[2]
    s[3] -= 1
    mr, mc = r // 3, c // 3
    
    # Evaluate if local board was just won/tied
    local_result = evaluateGrid3x3(s[0], mr * 3, mc * 3)
    if local_result != 0:
        s[4][mr][mc] = local_result
        
    # Evaluate if the entire game was won/tied based on the macro board
    global_result = evaluateGrid3x3(s[4])
    if global_result == COMPUTER:
        s[1] = VIC
        s[2] = COMPUTER + HUMAN - s[2] # Switch turn
        return
    elif global_result == HUMAN:
        s[1] = LOSS
        s[2] = COMPUTER + HUMAN - s[2]
        return
    elif s[3] == 0 or global_result == TIE_BOARD:
        s[1] = TIE
        s[2] = COMPUTER + HUMAN - s[2]
        return
        
    # Set constraint for the NEXT player's move
    next_mr, next_mc = r % 3, c % 3
    if s[4][next_mr][next_mc] != 0:
        s[5] = (-1, -1) # Target board is inactive, next player can play anywhere
    else:
        s[5] = (next_mr, next_mc)
        
    # Recalculate heuristic and switch turn
    s[1] = getHeuristicVal(s)
    s[2] = COMPUTER + HUMAN - s[2]
    
def inputMove(s):
    # Reads, enforces legality and executes the user's move.
    printState(s)
    flag = True
    while flag:
        try:
            move_str = input("Enter row and col separated by a space (e.g., '4 5'): ")
            parts = move_str.split()
            if len(parts) != 2:
                raise ValueError
            r, c = int(parts[0]), int(parts[1])
            
            if not isLegal(s, r, c):
                print("Illegal move. Please check the constraints and try an empty cell.")
            else:
                flag = False
                makeMove(s, r, c)
        except ValueError:
            print("Invalid input format. Please enter two numbers separated by a space.")

def getNext(s):
    # Generates all possible next states from current state
    ns = []
    
    # Generate legal moves
    for r in range(9):
        for c in range(9):
            if isLegal(s, r, c):
                tmp = copy.deepcopy(s)
                makeMove(tmp, r, c)
                ns.append(tmp)
                
    # Optimization: Sort the next states to massively improve Alpha-Beta Pruning efficiency
    if s[2] == COMPUTER:
        # MAX turn: explore paths with highest heuristic value first
        ns.sort(key=lambda x: x[1], reverse=True)
    else:
        # MIN turn: explore paths with lowest heuristic value first
        ns.sort(key=lambda x: x[1], reverse=False)
        
    return ns