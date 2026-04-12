from sqlalchemy.orm import Session
from models.models import Expense, Category
from datetime import date

class ExpenseManager:
    """
    Handles operations related to Expenses: Add, View, Delete.
    """
    def __init__(self, db_session: Session):
        self.db = db_session

    def add_expense(self, title, amount, category_name, expense_date):
        """
        Adds a new expense to the database.
        Finds the category by name first.
        """
        # 1. Find the category object from the name
        category = self.db.query(Category).filter(Category.name == category_name).first()
        
        if not category:
            print(f"Error: Category '{category_name}' not found.")
            return

        # 2. Create the Expense object
        new_expense = Expense(
            title=title,
            amount=amount,
            date=expense_date,
            category_id=category.id
        )

        # 3. Add to session and commit
        try:
            self.db.add(new_expense)
            self.db.commit()
            print("Expense added successfully!")
        except Exception as e:
            print(f"Error adding expense: {e}")
            self.db.rollback()

    def view_expenses(self):
        """
        Retrieves and displays all expenses, ordered by date.
        """
        expenses = self.db.query(Expense).order_by(Expense.date.desc()).all()
        
        if not expenses:
            print("\nNo expenses found.")
            return

        print("\n--- Expense List ---")
        print(f"{'ID':<5} {'Date':<12} {'Category':<15} {'Title':<20} {'Amount':<10}")
        print("-" * 65)
        for exp in expenses:
            cat_name = exp.category.name if exp.category else "Unknown"
            print(f"{exp.id:<5} {exp.date} {cat_name:<15} {exp.title:<20} ${exp.amount:<10.2f}")

    def delete_expense(self, expense_id):
        """
        Deletes an expense by its ID.
        """
        expense = self.db.query(Expense).filter(Expense.id == expense_id).first()
        
        if not expense:
            print(f"Error: Expense with ID {expense_id} not found.")
            return

        try:
            self.db.delete(expense)
            self.db.commit()
            print("Expense deleted successfully!")
        except Exception as e:
            print(f"Error deleting expense: {e}")
            self.db.rollback()

    def search_expenses_by_date(self, search_date):
        """
        Finds expenses for a specific date.
        """
        expenses = self.db.query(Expense).filter(Expense.date == search_date).all()
        
        if not expenses:
            print(f"\nNo expenses found on {search_date}.")
            return

        print(f"\n--- Expenses on {search_date} ---")
        for exp in expenses:
             print(f"{exp.title} - ${exp.amount} ({exp.category.name})")

