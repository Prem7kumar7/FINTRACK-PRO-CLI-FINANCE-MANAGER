from sqlalchemy import create_engine, Column, Integer, String, Float, Date, ForeignKey, text               # import 
from sqlalchemy.orm import declarative_base, sessionmaker, relationship
from datetime import datetime
engine = create_engine("sqlite:///fintrack.db", echo=True)
Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()

class Category(Base):
    __tablename__ = "categories"

    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True)

    expenses = relationship("Expense", back_populates="category")

class Expense(Base):
    __tablename__ = "expenses"

    id = Column(Integer, primary_key=True)
    title = Column(String)
    amount = Column(Float)
    date = Column(Date)

    category_id = Column(Integer, ForeignKey("categories.id"))
    category = relationship("Category", back_populates="expenses")
    
class Budget(Base):
    __tablename__ = "budgets"

    id = Column(Integer, primary_key=True)
    month = Column(String)          
    limit = Column(Float)

Base.metadata.create_all(engine)

def add_category():
    name = input("Category name: ")
    session.add(Category(name=name))
    session.commit()
    print("Category added")


def add_expense():
    title = input("Expense title: ")
    amount = float(input("Amount: "))
    date = datetime.strptime(input("Date (YYYY-MM-DD): "), "%Y-%m-%d").date()
    category_id = int(input("Category ID: "))

    session.add(
        Expense(
            title=title,
            amount=amount,
            date=date,
            category_id=category_id
        )
    )
    session.commit()
    print("Expense added")

def update_expense():
    eid = int(input("Expense ID: "))
    expense = session.query(Expense).filter(Expense.id == eid).first()

    if expense:
        expense.amount = float(input("New amount: "))
        session.commit()
        print("Expense updated")
    else:
        print("Expense not found")


def delete_expense():
    eid = int(input("Expense ID: "))
    expense = session.query(Expense).filter(Expense.id == eid).first()

    if expense:
        session.delete(expense)
        session.commit()
        print("Expense deleted")
    else:
        print("Expense not found")


def view_expenses():
    expenses = session.query(Expense).all()
    for e in expenses:
        print(e.id, e.title, e.amount, e.date)

def search_by_date():
    date = datetime.strptime(input("Enter date (YYYY-MM-DD): "), "%Y-%m-%d").date()
    expenses = session.query(Expense).filter(Expense.date == date).all()

    for e in expenses:
        print(e.title, "→", e.amount)

def category_report():
    sql = """
    SELECT categories.name, SUM(expenses.amount)
    FROM categories
    JOIN expenses ON categories.id = expenses.category_id
    GROUP BY categories.name
    """
    result = session.execute(text(sql))

    print("\n Category Wise Expense Report")
    for row in result:
        print(row[0], "→", row[1])

def set_budget():
    month = input("Month (YYYY-MM): ")
    limit = float(input("Budget limit: "))

    session.add(Budget(month=month, limit=limit))
    session.commit()
    print("Budget set")


def check_budget():
    month = input("Month (YYYY-MM): ")

    result = session.execute(
        text("SELECT SUM(amount) FROM expenses WHERE date LIKE :m"),
        {"m": f"{month}%"}
    ).fetchone()

    total = result[0] if result[0] else 0

    budget = session.query(Budget).filter(Budget.month == month).first()

    if budget and total > budget.limit:
        print("Budget exceeded")
    else:
        print("Budget under control")

while True:
    print("""
===== FINTRACK PRO =====
1. Add Category
2. Add Expense
3. Update Expense
4. Delete Expense
5. View Expenses
6. Search Expense by Date
7. Category Expense Report
8. Set Monthly Budget
9. Check Budget Status
10. Exit
""")

    choice = input("Choose: ")

    if choice == "1":
        add_category()
    elif choice == "2":
        add_expense()
    elif choice == "3":
        update_expense()
    elif choice == "4":
        delete_expense()
    elif choice == "5":
        view_expenses()
    elif choice == "6":
        search_by_date()
    elif choice == "7":
        category_report()
    elif choice == "8":
        set_budget()
    elif choice == "9":
        check_budget()
    elif choice == "10":
        print("Exiting FinTrack Pro")
        break
    else:
        print("Invalid choice")






    

