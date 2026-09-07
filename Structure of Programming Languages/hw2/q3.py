from functools import reduce

def is_armstrong(n: int) -> bool:
    """
    A pure function that checks if a positive integer is an Armstrong number.
    Returns True if it is, False otherwise.
    """
    # Convert the number to a string to easily iterate over its digits
    digits_str = str(n)
    k = len(digits_str)
    
    # Sum each digit raised to the power of k.
    # The string characters are mapped to integers implicitly inside the lambda.
    armstrong_sum = reduce(lambda acc, digit: acc + int(digit) ** k, digits_str, 0)
    
    return armstrong_sum == n

def armstrong_range(n1: int, n2: int) -> list:
    """
    Returns a list of all Armstrong numbers in the range between n1 and n2 (inclusive).
    """
    # Generate the range of numbers
    numbers_in_range = range(n1, n2 + 1)
    
    # Filter the numbers using the pure function
    armstrong_numbers = list(filter(is_armstrong, numbers_in_range))
    
    return armstrong_numbers

def main():
    """
    Main script that receives a number from the user, validates it,
    and prints all Armstrong numbers up to it.
    """
    user_input = input("Enter a positive integer: ")
    
    # Validate the input: must be composed only of digits and greater than 0
    if not user_input.isdigit() or int(user_input) <= 0:
        print("invalid input")
        return
    
    # Convert the valid input to an integer and call the range function
    limit = int(user_input)
    result = armstrong_range(1, limit)
    
    # Print the result
    print(f"Armstrong numbers between 1 and {limit}: {result}")

if __name__ == "__main__":
    main()