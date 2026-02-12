# FINTRACK-PRO-CLI-FINANCE-MANAGER
FinTrack Pro is a Command Line based Personal Finance Management System built using Python, SQLite, and SQLAlchemy ORM.

This project allows users to manage daily expenses, track categories, set monthly budgets, and generate financial reports using both ORM and Raw SQL queries.

---

## 🚀 Features

- Add Expense
- Update Expense
- Delete Expense
- Search Expense by Date
- Category-wise Expense Report (Using JOIN & GROUP BY)
- Set Monthly Budget
- Budget Alert System
- Persistent SQLite Database

---

## 🛠 Technologies Used

- Python
- SQLite
- SQLAlchemy ORM
- Raw SQL Queries
- CLI (Command Line Interface)

---

## 🗂 Database Structure

### 1️⃣ categories
| Column | Type |
|--------|------|
| id | Integer (Primary Key) |
| name | String |

### 2️⃣ expenses
| Column | Type |
|--------|------|
| id | Integer (Primary Key) |
| title | String |
| amount | Float |
| date | String |
| category_id | Foreign Key → categories.id |

### 3️⃣ budgets
| Column | Type |
|--------|------|
| id | Integer (Primary Key) |
| month | String (YYYY-MM) |
| limit | Float |

---

## 🔗 Relationships

- One Category → Many Expenses
- Foreign Key used to maintain referential integrity
- Bidirectional relationship using `relationship()` and `back_populates`

---

## 📊 SQL Concepts Used

- INSERT
- SELECT
- UPDATE
- DELETE
- JOIN
- GROUP BY
- SUM()
- WHERE
- LIKE
- Foreign Key

---

## 📈 Sample SQL Query Used

```sql
SELECT categories.name, SUM(expenses.amount)
FROM categories
JOIN expenses ON categories.id = expenses.category_id
GROUP BY categories.name;

## 🔄 Project Flow

1. User selects an option from CLI menu.
2. System performs database operation using SQLAlchemy ORM.
3. Data is stored in SQLite database (fintrack.db).
4. Reports use raw SQL queries with JOIN and GROUP BY.
5. Budget module compares monthly expense with set limit.
6. Alert is generated if spending exceeds budget.
7. Data persists between program runs.
