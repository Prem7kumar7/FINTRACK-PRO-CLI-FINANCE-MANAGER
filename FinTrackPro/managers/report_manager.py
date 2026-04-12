from sqlalchemy.orm import Session
from sqlalchemy import text

class ReportManager:
    """
    Handles report generation using raw SQL queries for analytics.
    """
    def __init__(self, db_session: Session):
        self.db = db_session

    def generate_category_report(self):
        """
        Shows total spending per category using a raw SQL query.
        Demonstrates JOIN and GROUP BY.
        """
        # Raw SQL query
        # We join 'categories' and 'expenses' tables
        sql_query = text("""
            SELECT c.name, SUM(e.amount) as total
            FROM categories c
            JOIN expenses e ON c.id = e.category_id
            GROUP BY c.name
            ORDER BY total DESC;
        """)

        try:
            result = self.db.execute(sql_query)
            rows = result.fetchall()

            print("\n--- Category-wise Spending (Raw SQL) ---")
            if not rows:
                print("No data available.")
                return

            print(f"{'Category':<20} {'Total Amount':<15}")
            print("-" * 35)
            for row in rows:
                # row is a tuple-like object (name, total)
                cat_name = row[0]
                total = row[1]
                print(f"{cat_name:<20} ${total:<15.2f}")
                
        except Exception as e:
            print(f"Error generating report: {e}")

    def export_csv_placeholder(self):
        print("CSV Export feature coming soon!")
