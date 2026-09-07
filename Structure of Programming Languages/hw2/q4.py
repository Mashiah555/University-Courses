from datetime import datetime, timedelta

def get_gregorian_dates(start_date_str: str, num_dates: int, skip_days: int) -> list:
    """
    Generates a list of Gregorian dates starting from a given date string,
    skipping a specified number of days between each date.
    
    Args:
        start_date_str: The starting date as a string (e.g., '2026-09-07').
        num_dates: The total number of dates to generate.
        skip_days: The number of days to skip between each date.
        
    Returns:
        A list of formatted date strings.
    """
    # Parse the starting date string into a datetime object
    start_date = datetime.strptime(start_date_str, "%Y-%m-%d")
    
    # Lambda function to calculate the new date based on the index multiplier
    # It adds (index * skip_days) to the starting date and formats it back to a string
    date_calculator = lambda i: (start_date + timedelta(days=i * skip_days)).strftime("%Y-%m-%d")
    
    # Apply the calculation over the requested number of dates
    dates_list = list(map(date_calculator, range(num_dates)))
    
    return dates_list
  
def get_hebrew_dates(start_date_str: str, num_dates: int, skip_days: int) -> list:
    """
    Generates a list of Hebrew dates starting from a given Hebrew date string,
    skipping a specified number of days.
    
    Args:
        start_date_str: The starting date 'YYYY-MM-DD' representing Hebrew year, month, day.
        num_dates: The total number of dates to generate.
        skip_days: The number of days to skip between each date.
    """
    from pyluach.dates import HebrewDate

    # Parse the input string into year, month, and day integers
    year, month, day = map(int, start_date_str.split('-'))
    start_hebrew_date = HebrewDate(year, month, day)
    
    # Lambda function to calculate the new Hebrew date by adding days
    hebrew_date_calculator = lambda i: str(start_hebrew_date + (i * skip_days))
    
    # Generate the list of dates
    hebrew_dates_list = list(map(hebrew_date_calculator, range(num_dates)))
    
    return hebrew_dates_list


def main():
    """
    Main execution script to demonstrate the date functions.
    """
    print("--- Part A: Gregorian Dates ---")
    start_gregorian = "2026-09-07"
    num_dates = 5
    skip_days = 7
    
    greg_results = get_gregorian_dates(start_gregorian, num_dates, skip_days)
    print(f"Starting date: {start_gregorian}, Generating {num_dates} dates with {skip_days} days skip:")
    for d in greg_results:
        print(d)
        
    print("\n--- Optional Part B: Hebrew Dates ---")
    start_hebrew = "5787-01-01"

    heb_results = get_hebrew_dates(start_hebrew, num_dates, skip_days)
    print(f"Starting Hebrew date: {start_hebrew}, Generating {num_dates} dates with {skip_days} days skip:")
    for d in heb_results:
        print(d)

if __name__ == "__main__":
    main()