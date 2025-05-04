import csv
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

# Expense Class
class Expense:
    def __init__(self, amount, category, date):
        self.amount = amount
        self.category = category
        self.date = date

# File Operations
def save_expense(expense):
    with open('expenses.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([expense.amount, expense.category, expense.date])

def load_expenses():
    expenses = []
    try:
        with open('expenses.csv', 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                expenses.append(Expense(float(row[0]), row[1], row[2]))
    except FileNotFoundError:
        pass
    return expenses

# Data Analysis
def analyze_expenses(expenses):
    df = pd.DataFrame([(e.amount, e.category, e.date) for e in expenses], columns=['Amount', 'Category', 'Date'])
    print("\nExpense Summary:")
    print(df.groupby('Category').sum())

    # Visualization
    df.groupby('Category').sum().plot(kind='bar')
    plt.title('Expense Distribution by Category')
    plt.xlabel('Category')
    plt.ylabel('Amount')
    plt.show()

# CLI Interface
def main():
    while True:
        print("\nExpense Tracker Menu:")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Analyze Expenses")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            amount = float(input("Enter amount: "))
            category = input("Enter category: ")
            date = datetime.now().strftime('%Y-%m-%d')
            expense = Expense(amount, category, date)
            save_expense(expense)
            print("Expense added successfully!")

        elif choice == '2':
            expenses = load_expenses()
            for expense in expenses:
                print(f"Amount: {expense.amount}, Category: {expense.category}, Date: {expense.date}")

        elif choice == '3':
            expenses = load_expenses()
            analyze_expenses(expenses)

        elif choice == '4':
            print("Exiting Expense Tracker. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()