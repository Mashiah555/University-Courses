# Yuval Mashiah
# 329245161
# Exercise 1 Submittion
import math
import ast
import random

# --- Boolfuncs Module ---
def isNumber(valStr):
   if valStr.count('.') > 1:
     return False
   L = [c for c in valStr  if (c.isdigit() or c == '.')]
   return len(L) == len(valStr)
#
def getNumber(prompt):
   while True:
     val = input(prompt)
     if not isNumber(val):
       print ("it must be a number!")
     else:
       return eval(val)
     
# --- QUESTION 1 ---

def isValidTriangle(a, b, c):
    """
    Checks if the 3 numbers can be the sides of a valid triangle
    """
    return ((a + b) > c and (a + c) > b and (b + c) > a)

def q1():
    n1 = getNumber("Please enter the first number: ")
    n2 = getNumber("Please enter the second number: ")
    n3 = getNumber("Please enter the third number: ")
    if isValidTriangle(n1, n2, n3):
        print("Correct triangle sides lengths")
    else:
        print("Not correct triangle sides lengths")

# --- QUESTION 2 ---

# Area calculation functions
def rectangleArea(w, h):
     return w * h
#
def circleArea(r):
     return math.pi * r**2
#
def triangleArea(a, b, c):
     s = (a + b + c) / 2
     return math.sqrt(s * (s - a) * (s - b) * (s - c))
#
def squareArea(s):
    return s**2
#
def sphereVolume(r):
    return 4/3 * math.pi * r**3
#
def cylinderVolume(r, h):
    return math.pi * r**2 * h
#
def coneVolume(r, h):
    return 1/3 * cylinderVolume(r, h)
#
def cubeVolume(s):
    return s**3
#
def squarePyramidVolume(s, h):
    return 1/3 * s**2 * h

# printing the menu options
def prtMenu(shapes):
   for i in range(len(shapes)):
      print (i+1, shapes[i])
   return

def q2():
    print ("Welcome to the Area calculation program")
    print ("---------------------------------------\n")  
    # Print out the menu
    shapes = ("Rectangle", "Circle", "Triangle", "Square", "Sphere", "Cylinder", "Cone", "Cube", "Square Pyramid")
    while True:
        print ("\nPlease select a shape (press 0 to quit to main menu):")
        prtMenu(shapes) 
        # Get the user's choice: 
        shape = input("> ")
        # Calculate the area: 
        if shape == "1":
            height = getNumber("Please enter the height: ")    
            width  = getNumber("Please enter the width: ")
            area = rectangleArea(width, height)
            print ("The area is", area)
            continue
        elif shape == "2":
            radius = getNumber("Please enter the radius: ")
            area   = circleArea(radius)
            print ("The area is", area)
            continue
        elif shape == "3":
            a = getNumber("Please enter the first side: ")
            b = getNumber("Please enter the second side: ")
            c = getNumber("Please enter the third side: ")
            area = triangleArea(a, b, c)
            print ("The area is", area)
            continue
        elif shape == "4":
            side = getNumber("Please enter the side: ")
            area = squareArea(side)
            print ("The area is", area)
            continue
        elif shape == "5":
            radius = getNumber("Please enter the radius: ")
            area   = sphereVolume(radius)
            print ("The volume is", area)
            continue
        elif shape == "6":
            radius = getNumber("Please enter the radius: ")
            height = getNumber("Please enter the height: ")
            area   = cylinderVolume(radius, height)
            print ("The volume is", area)
            continue
        elif shape == "7":
            radius = getNumber("Please enter the radius: ")
            height = getNumber("Please enter the height: ")
            area   = coneVolume(radius, height)
            print ("The volume is", area)
            continue
        elif shape == "8":
            side = getNumber("Please enter the side: ")
            area = cubeVolume(side)
            print ("The volume is", area)
            continue
        elif shape == "9":
            side = getNumber("Please enter the side: ")
            height = getNumber("Please enter the height: ")
            area = squarePyramidVolume(side, height)
            print ("The volume is", area)
            continue
        elif shape == "0":
            print ("Bye!")
            break
        else:     
            print ("Invalid shape")

# --- QUESTION 3 ---

def getFourUniqueNumbers():
    """
    Returns a list of 4 DIFFERENT numbers from the user.
    """
    unique_numbers = []
    
    while len(unique_numbers) < 4:
        # Prompt the user, indicating how many numbers we currently have
        prompt = f"Please enter number {len(unique_numbers) + 1}: "
        current_number = getNumber(prompt)
        
        # Check if the number is already in our list
        if current_number not in unique_numbers:
            unique_numbers.append(current_number)
        else:
            print("You already entered that number! Please choose a different one.")
            
    return unique_numbers

def printMiddleNumbersSorted(numbers):
    """
    Prints the two middle numbers using the built-in sort function.
    """
    numbers.sort()
    n = len(numbers)
    
    # Ensure the list isn't empty before trying to find the middle
    if n == 0 or n % 2 != 0:
        print("Error: List must contain an even, non-zero amount of numbers.")
        return
        
    # Calculate the middle indices dynamically
    midIndex = n // 2
    middle1 = numbers[midIndex - 1]
    middle2 = numbers[midIndex]
    
    print("The two middle numbers are", middle1, "and", middle2)

def printMiddleNumbersManual(nums):
    """
    Prints the two middle numbers without using any built-in functions.
    """    
    n = len(nums)
    
    # Ensure the list is even and not empty
    if n == 0 or n % 2 != 0:
        print("Error: Please provide a list with an even, non-zero amount of numbers.")
        return

    # Sort the list manually (Bubble Sort)
    for i in range(n):
        for j in range(0, n - i - 1):
            if nums[j] > nums[j + 1]:
                # Swap the elements if they are out of order
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
                
    # Find the two middle numbers
    # For an even length list, the middle indices are (n / 2) - 1 and (n / 2)
    midIndex = n // 2
    middle1 = nums[midIndex - 1]
    middle2 = nums[midIndex]
    
    print(f"The two middle numbers are {middle1} and {middle2}")

def q3a():
    numbers = getFourUniqueNumbers()
    print("\nUsing the built-in sort function:")
    printMiddleNumbersSorted(numbers)
    print("\nUsing manual sorting:")
    printMiddleNumbersManual(numbers)

def q3b(numrecord):
    # Helper function to flatten a nested tuple/list
    def flatten_values(record):
        flat_list = []
        for item in record:
            if isinstance(item, (list, tuple)):
                # If it's a nested sequence, dive into it
                flat_list.extend(flatten_values(item))
            else:
                # Otherwise, it's a number we can add
                flat_list.append(item)
        return flat_list
    #

    numList = flatten_values(numrecord)

    print("\nUsing the built-in sort function:")
    printMiddleNumbersSorted(numList)
    print("\nUsing manual sorting:")
    printMiddleNumbersManual(numList)

def extract_numeric_values(record):
    """
    Recursively filters a sequence (Tuple or List) to return a new sequence 
    containing only the numeric values (ints and floats), preserving the original type.
    """
    # If the record isn't a list or tuple, return an empty version of it or None
    if not isinstance(record, (list, tuple)):
        return []

    numeric_record = []
    
    for item in record:
        # If the item is a nested tuple/list, call this function recursively
        if isinstance(item, (list, tuple)):
            nested_result = extract_numeric_values(item)
            if nested_result: # Only add if it's not empty
                numeric_record.append(nested_result)
                
        # If the item is a number, add it to the new record
        elif isinstance(item, (int, float)) and not isinstance(item, bool):
            numeric_record.append(item)
            
    # Convert the result back to a Tuple if the original record was a Tuple
    if isinstance(record, tuple):
        return tuple(numeric_record)
    
    return numeric_record

def q3c(record):
    numeric_record = extract_numeric_values(record)
    q3b(numeric_record)

def q3():
    print ("Question 3 Sub-Menu")
    print ("---------------------------------------\n")  
    # Print out the menu
    questions = ("Sub-question A", "Sub-question B", "Sub-question C")
    while True:
        print ("\nPlease select a sub-question (press 0 to quit to main menu):")
        prtMenu(questions) 
        # Get the user's choice: 
        choice = input("> ")
        # Calculate the area: 
        if choice == "1":
            q3a()
            continue
        elif choice == "2":
            record = input("Enter a numeric record: ")
            try:
                q3b(ast.literal_eval(record))
            except (ValueError, SyntaxError):
                print("Invalid input format!")
            continue
        elif choice == "3":
            record = input("Enter a flat or nested record of different value types: ")
            try:
                q3c(ast.literal_eval(record))
            except (ValueError, SyntaxError):
                print("Invalid input format!")
            continue
        elif choice == "0":
            print ("Bye!")
            break
        else:     
            print ("Invalid Selection")

# --- QUESTION 4 ---

def shiftL(binNr, N):
    """
    Shifts the binary string left by N places[cite: 35].
    The leftmost N digits fall off, and N '0's are added to the right[cite: 35].
    """
    # Protect against N being larger than the string length
    N = min(N, len(binNr))
    return binNr[N:] + '0' * N

def shiftR(binNr, N):
    """
    Shifts the binary string right by N places[cite: 35].
    The rightmost N digits fall off, and N '0's are added to the left[cite: 35].
    """
    N = min(N, len(binNr))
    return '0' * N + binNr[:-N]

def shiftCL(binNr, N):
    """
    Circularly shifts the binary string left by N places[cite: 35].
    The leftmost N digits are moved to the right side[cite: 35].
    """
    N = N % len(binNr) 
    return binNr[N:] + binNr[:N]

def shiftCR(binNr, N):
    """
    Circularly shifts the binary string right by N places[cite: 35].
    The rightmost N digits are moved to the left side[cite: 35].
    """
    N = N % len(binNr)
    return binNr[-N:] + binNr[:-N]

def q4():
    print ("Question 4 Sub-Menu")
    print ("---------------------------------------\n")  
    # Print out the menu
    options = ("Shift Left", "Shift Right", "Circular Shift Left", "Circular Shift Right")
    while True:
        print ("\nPlease select the shift type (press 0 to quit to main menu):")
        prtMenu(options) 
        # Get the user's choice: 
        choice = input("> ")
        str = input("Enter a binary string: ")
        shift = int(input("Enter the number of places to shift: "))
        # Calculate the area: 
        if choice == "1":
            print(shiftL(str, shift))
            continue
        elif choice == "2":
            print(shiftR(str, shift))
            continue
        elif choice == "3":
            print(shiftCL(str, shift))
            continue
        elif choice == "4":
            print(shiftCR(str, shift))
            continue
        elif choice == "0":
            print ("Bye!")
            break
        else:     
            print ("Invalid Selection")


# --- QUESTION 5 ---

def count_data_types(data_list):
    """
    Counts the occurrences of different data types in a given list.
    Returns a dictionary where the keys are the type names and the values are the counts.
    """
    # Initialize the dictionary with the required types as keys
    type_counts = {list: 0, int: 0, float: 0, str: 0, tuple: 0}
    
    # Iterate through the list using a for loop to count types
    for item in data_list:
        item_type = type(item)
        if item_type in type_counts:
            type_counts[item_type] += 1
            
    return type_counts

def q5():
    L = list(input("Enter a list of values: "))
    counts_dict = count_data_types(L)

    total_numbers = counts_dict[int] + counts_dict[float]
    total_tuples = counts_dict[tuple]
    total_lists = counts_dict[list]
    total_strings = counts_dict[str]

    print(f'Total Tuples: {total_tuples}, '
        f'Total Lists: {total_lists}, '
        f'Total Numbers: {total_numbers}, '
        f'Total Strings: {total_strings}')

# --- QUESTION 6 ---

def nihushTest(secret_tuple, *guesses):
    """
    Compares the secret_tuple against an unknown number of guessed integers.
    Returns a tuple with the correct number in its position, or 'X' if the guess was wrong.
    """
    result = []
    
    # Iterate through the length of the secret tuple
    for i in range(len(secret_tuple)):
        # Check if the user provided enough guesses and if the guess matches the secret
        if i < len(guesses) and guesses[i] == secret_tuple[i]:
            result.append(guesses[i])
        else:
            result.append("X")
            
    return tuple(result)

def q6():
    # 1. Generate N random numbers between 1 and 9 (where 3 <= N <= 9)
    N = random.randint(3, 9)
    secret_tuple = tuple(random.randint(1, 9) for _ in range(N))
    
    # We shouldn't print the secret tuple during actual gameplay, 
    # but uncomment the next line if you want to test it easily:
    print(f"[DEBUG] Secret is {secret_tuple}")
    
    maxpct = 0.0
    print(f"--- Welcome to the Guessing Game! ---")
    print(f"There were randomly chosen {N} numbers between 1 and 9.")
    
    # Game Loop
    while True:
        # Prompt the user for their guesses or to quit
        user_input = input(f"\nEnter your {N} guesses separated by spaces (or -1 to quit to main menu): ").strip()
        
        # Check for the quit condition
        if user_input == "-1":
            print("You chose to quit.")
            break
            
        # Safely parse the user input into a list of integers
        try:
            guess_list = [int(x) for x in user_input.split()]
        except ValueError:
            print("Invalid input! Please enter only integers.")
            continue
            
        # Ensure the user entered exactly N numbers
        if len(guess_list) != N:
            print(f"You entered {len(guess_list)} numbers. Please enter exactly {N} numbers.")
            continue
            
        # Convert the list to a tuple
        guess_tuple = tuple(guess_list)
        
        # Call nihushTest using the * operator to unpack the tuple into individual arguments
        result_tuple = nihushTest(secret_tuple, *guess_tuple)
        
        # Calculate the success percentage
        correct_count = sum(1 for item in result_tuple if item != "X")
        current_pct = (correct_count / N) * 100.0
        
        # Update maxpct if the current guess is the best one yet
        if current_pct > maxpct:
            maxpct = current_pct
            
        # Print the resulting tuple and the percentage on the same line
        print(f"Result: {result_tuple} | Success: {current_pct:.2f}%")
        
        # Check if the guess was perfect
        if correct_count == N:
            print("Congratulations! Your guess was perfect!")
            break

    # When the game ends (either by -1 or by winning), print the final stats
    print("\n--- Game Over ---")
    print(f"The randomly chosen numbers were: {secret_tuple}")
    print(f"Your highest success percentage (maxpct): {maxpct:.2f}%")

# --- MAIN MENU ---

def main():
    funcList = [q1, q2, q3, q4, q5, q6]
    descList = ["Exit the program", "Question 1", "Question 2", "Question 3", "Question 4", "Question 5", "Question 6"]

    while True:
        print("Your choices:")
        for (i, s) in enumerate(descList):
            print(i, " : ", s)
        c = int(input("Please enter your choice: "))
        if c == 0:
            break
        elif 1 <= c <= len(descList):
            funcList[c - 1]()
        else:
            print("Error")

if __name__ == "__main__":
    main()