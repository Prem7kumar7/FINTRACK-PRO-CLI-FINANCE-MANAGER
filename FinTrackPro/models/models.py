from sqlalchemy import Column, Integer, String, Float, Date, ForeignKey
from sqlalchemy.orm import relationship, declarative_base

# Define the base class for all our models
# This is a factory function that constructs a base class for declarative models
Base = declarative_base()

class Category(Base):
    """
    Represents a category for expenses (e.g., Food, Travel, Bills).
    """
    __tablename__ = 'categories'

    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True, nullable=False)

    # Relationship to expenses: One Category -> Many Expenses
    expenses = relationship("Expense", back_populates="category")

    def __repr__(self):
        return f"<Category(name='{self.name}')>"

class Expense(Base):
    """
    Represents an individual expense record.
    """
    __tablename__ = 'expenses'

    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    amount = Column(Float, nullable=False)
    date = Column(Date, nullable=False)
    
    # Foreign Key linking to the Category table
    category_id = Column(Integer, ForeignKey('categories.id'), nullable=False)
    
    # Relationship back to the Category model
    category = relationship("Category", back_populates="expenses")

    def __repr__(self):
        return f"<Expense(title='{self.title}', amount={self.amount}, date='{self.date}')>"

class Subscription(Base):
    """
    Represents a recurring subscription.
    """
    __tablename__ = 'subscriptions'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    amount = Column(Float, nullable=False)
    next_due_date = Column(Date, nullable=False)

    def __repr__(self):
        return f"<Subscription(name='{self.name}', amount={self.amount})>"

class Budget(Base):
    """
    Represents a monthly budget limit.
    """
    __tablename__ = 'budgets'

    id = Column(Integer, primary_key=True)
    month = Column(String, nullable=False)  # Format: "YYYY-MM"
    limit = Column(Float, nullable=False)

    def __repr__(self):
        return f"<Budget(month='{self.month}', limit={self.limit})>"
