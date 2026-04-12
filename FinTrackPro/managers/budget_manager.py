from sqlalchemy.orm import Session
from sqlalchemy import func
from models.models import Budget, Expense
from datetime import date

class BudgetManager:
    """
    Handles monthly budget setting and checking.
    """
    def __init__(self, db_session: Session):
        self.db = db_session

    def set_budget(self, month, amount):
        """
        Sets or updates the budget for a specific month (YYYY-MM).
        """
        # Check if budget already exists for this month
        budget = self.db.query(Budget).filter(Budget.month == month).first()

        if budget:
            budget.limit = amount
            print(f"Updated budget for {month} to ${amount:.2f}")
        else:
            new_budget = Budget(month=month, limit=amount)
            self.db.add(new_budget)
            print(f"Set budget for {month} to ${amount:.2f}")

        try:
            self.db.commit()
        except Exception as e:
            print(f"Error setting budget: {e}")
            self.db.rollback()

    def check_budget(self, month):
        """
        Compares total spending against the budget for a given month.
        """
        # 1. Get the budget limit
        budget = self.db.query(Budget).filter(Budget.month == month).first()
        if not budget:
            print(f"No budget set for {month}.")
            return

        # 2. Calculate total expenses for that month
        # We need to filter expenses where the date string starts with YYYY-MM
        # SQLite function 'strftime' can be used
        
        # total_spent = self.db.query(func.sum(Expense.amount)).filter(
        #     func.strftime("%Y-%m", Expense.date) == month
        # ).scalar() or 0.0

        # Alternative python-side filtering for simplicity if SQL functions get tricky
        # But for learning, let's try the SQL way or start/end date range
        
        # Construct start and end dates for the month
        year, month_num = map(int, month.split('-'))
        # Simple logic: Filter >= 1st of month AND < 1st of next month
        import calendar
        _, last_day = calendar.monthrange(year, month_num)
        
        start_date = date(year, month_num, 1)
        end_date = date(year, month_num, last_day)

        total_spent = self.db.query(func.sum(Expense.amount)).filter(
            Expense.date >= start_date,
            Expense.date <= end_date
        ).scalar() or 0.0

        # 3. Compare and Report
        print(f"\n--- Budget Report for {month} ---")
        print(f"Limit:        ${budget.limit:.2f}")
        print(f"Total Spent:  ${total_spent:.2f}")
        
        remaining = budget.limit - total_spent
        if remaining < 0:
            print(f"WARNING: You have exceeded your budget by ${abs(remaining):.2f}!")
        else:
            print(f"Remaining:    ${remaining:.2f}")
