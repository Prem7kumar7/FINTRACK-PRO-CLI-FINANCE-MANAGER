import sys
from database import get_db, init_db, seed_data
from managers.expense_manager import ExpenseManager
from managers.budget_manager import BudgetManager
from managers.report_manager import ReportManager
from utils.common import get_valid_date, get_valid_amount, get_valid_month

def main_menu():
    print("\n=================================")
    print("   FINTRACK PRO - FINANCE MANAGER")
    print("=================================")
    print("1. Add New Expense")
    print("2. View All Expenses")
    print("3. Search Expenses by Date")
    print("4. Delete Expense")
    print("5. Set Monthly Budget")
    print("6. Check Budget Status")
    print("7. Generate Category Report (Analytics)")
    print("8. Exit")
    print("=================================")

def run():
    # 1. Initialize DB and Seed Data (ensure DB is ready)
    init_db()
    seed_data()

    # 2. Create a Database Session
    db = get_db()
    
    # 3. Initialize Managers with the session
    expense_manager = ExpenseManager(db)
    budget_manager = BudgetManager(db)
    report_manager = ReportManager(db)

    while True:
        main_menu()
        choice = input("Enter your choice (1-8): ")

        if choice == '1':
            print("\n--- Add Expense ---")
            title = input("Enter Title: ")
            amount = get_valid_amount()
            category = input("Enter Category (Food, Travel, etc.): ")
            date_obj = get_valid_date()
            expense_manager.add_expense(title, amount, category, date_obj)

        elif choice == '2':
            expense_manager.view_expenses()

        elif choice == '3':
            print("\n--- Search by Date ---")
            search_date = get_valid_date("Enter date to search (YYYY-MM-DD): ")
            expense_manager.search_expenses_by_date(search_date)

        elif choice == '4':
            print("\n--- Delete Expense ---")
            expense_manager.view_expenses() # Show list first so they know ID
            try:
                exp_id = int(input("Enter Expense ID to delete: "))
                expense_manager.delete_expense(exp_id)
            except ValueError:
                print("Invalid ID.")

        elif choice == '5':
            print("\n--- Set Budget ---")
            month = get_valid_month()
            limit = get_valid_amount("Enter budget limit: ")
            budget_manager.set_budget(month, limit)

        elif choice == '6':
            print("\n--- Check Budget ---")
            month = get_valid_month()
            budget_manager.check_budget(month)

        elif choice == '7':
            report_manager.generate_category_report()

        elif choice == '8':
            print("Exiting FinTrack Pro. Goodbye!")
            db.close()
            sys.exit()

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    try:
        run()
    except KeyboardInterrupt:
        print("\nProcess interrupted. Exiting...")
    except Exception as e:
        print(f"Unexpected error: {e}")
