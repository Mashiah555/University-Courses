# --- Part A: Pure Text Processing Functions ---

def clean_spaces(text: str) -> str:
    """
    Receives a string and returns it without leading or trailing spaces.
    """
    return text.strip()


def capitalize_text(text: str) -> str:
    """
    Receives a string and returns it with the first letter of each word capitalized.
    """
    return text.title()


def add_stars(text: str) -> str:
    """
    Receives a string and returns it surrounded by three asterisks on each side.
    """
    return f"***{text}***"


# --- Part B: Pipeline Management Functions ---

def create_pipeline():
    """
    Returns the base function of the pipeline (an identity function 
    that returns the input exactly as it is).
    """
    return lambda x: x


def add_to_pipeline(pipeline_fn, new_fn):
    """
    Receives an existing pipeline function and a new function.
    Returns a newly composed function that executes the existing pipeline first,
    and then applies the new function to its result.
    Strictly avoids loops and recursion.
    """
    return lambda x: new_fn(pipeline_fn(x))


# --- Part C: Main Script ---

def main():
    """
    Main script execution for the pipeline program.
    Builds the pipeline, receives user input, validates it, and processes it.
    """
    # Create a new pipeline 
    my_pipeline = create_pipeline()
    
    # Add the three functions from Part A in order
    my_pipeline = add_to_pipeline(my_pipeline, clean_spaces)
    my_pipeline = add_to_pipeline(my_pipeline, capitalize_text)
    my_pipeline = add_to_pipeline(my_pipeline, add_stars)
    
    # Get text from the user
    user_input = input("enter text:\n")
    
    # Check if the input is empty or contains only spaces
    if not user_input or user_input.isspace():
        print("invalid input")
    else:
        # Apply the composed pipeline to the input and print the result
        result = my_pipeline(user_input)
        print(result)


if __name__ == "__main__":
    main()