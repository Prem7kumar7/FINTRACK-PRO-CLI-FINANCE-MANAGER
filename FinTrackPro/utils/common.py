import datetime

def get_valid_date(prompt="Enter date (YYYY-MM-DD): "):
    """
    Prompts the user for a date and validates the format.
    Returns a datetime.date object.
    """
    while True:
        date_str = input(prompt)
        try:
            return datetime.datetime.strptime(date_str, "%Y-%m-%d").date()
        except ValueError:
            print("Invalid format. Please use YYYY-MM-DD.")

def get_valid_amount(prompt="Enter amount: "):
    """
    Prompts the user for a numeric amount and validates it.
    """
    while True:
        amount_str = input(prompt)
        try:
            amount = float(amount_str)
            if amount < 0:
                print("Amount cannot be negative.")
                continue
            return amount
        except ValueError:
            print("Invalid input. Please enter a number.")

def get_valid_month(prompt="Enter month (YYYY-MM): "):
    """
    Prompts for a month string in YYYY-MM format.
    """
    while True:
        month_str = input(prompt)
        try:
            datetime.datetime.strptime(month_str, "%Y-%m")
            return month_str
        except ValueError:
            print("Invalid format. Please use YYYY-MM.")
