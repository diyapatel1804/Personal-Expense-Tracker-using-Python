import sqlite3
from datetime import datetime

# Connect to database
conn = sqlite3.connect("expenses.db")
cursor = conn.cursor()

# Create table
cursor.execute("""
CREATE TABLE IF NOT EXISTS expenses (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    amount REAL,
    category TEXT,
    description TEXT,
    date TEXT
)
""")
conn.commit()

def add_expense():
    amount = float(input("Enter amount: "))
    category = input("Enter category (Food, Travel, etc): ")
    description = input("Enter description: ")
    date = datetime.now().strftime("%Y-%m-%d")

    cursor.execute(
        "INSERT INTO expenses (amount, category, description, date) VALUES (?, ?, ?, ?)",
        (amount, category, description, date)
    )
    conn.commit()
    print("✅ Expense added successfully")

def view_expenses():
    cursor.execute("SELECT * FROM expenses")
    rows = cursor.fetchall()

    print("\nID | Amount | Category | Description | Date")
    print("-" * 50)
    for row in rows:
        print(row)

def total_expense():
    cursor.execute("SELECT SUM(amount) FROM expenses")
    total = cursor.fetchone()[0]
    print(f"\n💵 Total Expense: ₹{total if total else 0}")

while True:
    print("\n=== Expense Tracker Menu ===")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Total Expense")
    print("4. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        add_expense()
    elif choice == "2":
        view_expenses()
    elif choice == "3":
        total_expense()
    elif choice == "4":
        print("👋 Exiting Expense Tracker")
        break
    else:
        print("❌ Invalid choice")
