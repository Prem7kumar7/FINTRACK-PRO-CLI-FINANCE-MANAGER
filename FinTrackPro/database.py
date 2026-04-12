from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.models import Base, Category
import os

# Define the database file path
# We use an absolute path or relative path. Here we store it in a 'data' folder.
DB_FOLDER = 'data'
DB_FILE = 'finance.db'
DB_PATH = os.path.join(DB_FOLDER, DB_FILE)

# Ensure the data directory exists
if not os.path.exists(DB_FOLDER):
    os.makedirs(DB_FOLDER)

# Create the Database Engine
# specific to SQLite, using 3 slashes for relative path
DATABASE_URL = f"sqlite:///{DB_PATH}"

# echo=False disables SQL logging (set to True to see raw SQL for learning)
engine = create_engine(DATABASE_URL, echo=False)

# Create a customized Session class
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def init_db():
    """
    Initializes the database by creating all tables defined in models.
    """
    print(f"Initializing database at {DB_PATH}...")
    Base.metadata.create_all(bind=engine)
    print("Database tables created successfully.")

def get_db():
    """
    Dependency that provides a database session.
    Use this in a context manager or try/finally block.
    """
    db = SessionLocal()
    try:
        return db
    except Exception:
        db.close()
        raise

def seed_data():
    """
    Populates the database with initial data (e.g., default categories).
    """
    session = SessionLocal()
    try:
        # Check if categories already exist
        if session.query(Category).first():
            print("Categories already exist. Skipping seed.")
            return

        print("Seeding default categories...")
        default_categories = [
            "Food", "Travel", "Bills", "Subscription", "Entertainment", "Medical", "Shopping", "Other"
        ]
        
        for cat_name in default_categories:
            category = Category(name=cat_name)
            session.add(category)
        
        session.commit()
        print("Default categories added.")
    except Exception as e:
        print(f"Error seeding data: {e}")
        session.rollback()
    finally:
        session.close()

if __name__ == "__main__":
    # If run directly, initialize and seed the DB
    init_db()
    seed_data()
