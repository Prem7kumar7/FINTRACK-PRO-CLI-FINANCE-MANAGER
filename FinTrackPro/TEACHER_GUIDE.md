# FinTrack Pro - Teacher's Guide (Project Explanation)

Ye guide aapko help karegi ki aap is project ko *Interview* ya *College Presentation* mein kaise explain karein.
Humne project ko **Modular Architecture** mein banaya hai, jo industry standard hai.

---

## 1. Project Structure (Framework)
**Interviewer:** "Aapne sab kuch ek file mein kyu nahi likha?"
**Answer:** "Sir, maine **Modular Approach** use kiya hai taaki code maintainable aur scalable ho."

*   **`models/`**: Sirf Database ka structure define karta hai (Tables).
*   **`managers/`**: Business logic handle karta hai (Add, Delete, Calculation).
*   **`utils/`**: Helper functions (jaise Date validation) jo har jagah kaam aate hain.
*   **`database.py`**: Database connection aur Session management ka kaam karta hai.
*   **`main.py`**: Sirf user se baat karta hai (Input/Output).

---

## 2. ORM vs Raw SQL (Technical Concept)
**Interviewer:** "SQLAlchemy ORM kyu use kiya?"
**Answer:** "ORM (Object Relational Mapper) hume Python Objects (`Expense`, `Category`) ke through database se baat karne deta hai, bina SQL likhe. Isse code clean rehta hai aur SQL Injection se bachat hoti hai."

*   **Example Code:**
    ```python
    # ORM Way (Clean Python)
    session.add(new_expense)
    session.commit()
    ```

**Interviewer:** "Kya tumhe raw SQL aati hai?"
**Answer:** "Haan sir, Reporting module mein maine complex joining ke liye Raw SQL likhi hai."
*   **Example (in `report_manager.py`):** `SELECT ... FROM ... JOIN ...`

---

## 3. Database Session Logic
Code mein humne `Session` use kiya hai.
*   **Session:** Ye ek "temporary workspace" hai jaha hum changes karte hain.
*   **Commit:** Jab tak `session.commit()` nahi karenge, database mein save nahi hoga.
*   **Rollback:** Agar koi error aaye, toh `session.rollback()` pure process ko cancel kar deta hai taaki data corrupt na ho.

---

## 4. One-to-Many Relationship
**Interviewer:** "Category aur Expense ka relation kya hai?"
**Answer:** "One-to-Many. Ek Category (jaise 'Food') mein bohot saare Expenses ho sakte hain (`Pizza`, `Burger`). Isliye `expenses` table mein `category_id` foreign key hai."

---

## 5. How to Run the Project
1.  Terminal kholiye project folder mein.
2.  Dependencies install karein:
    ```bash
    pip install sqlalchemy
    ```
3.  Project run karein:
    ```bash
    python main.py
    ```
    (Pehli baar run karne par ye automatically `finance.db` bana dega).

---

## Summary for Presentation
"Is project mein maine Python aur SQL ka use karke ek Finance Manager banaya hai. Maine **MVC pattern** (Model-View-Controller) se milta-julta structure follow kiya hai. Data save karne ke liye **SQLite** aur logic ke liye **Python** use kiya hai. Future mein main isme **Flask** jodkar isse web app bhi bana sakta hoon."
